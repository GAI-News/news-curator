from email.message import EmailMessage
from fastapi import FastAPI
import smtplib

from curator import CuratorBase, GPT, GPTZeroShotClassification, NewsCollector
from curator.backend.types import NewsRequestInput


class Server(CuratorBase):
    def __init__(self):
        super().__init__()
        self.newscollector = NewsCollector(sources=self.config['PATHS']['SOURCES'])
        self.news_df = None
        self.featured_clusters = None

    @classmethod
    def gpt_instructions(cls, tone: str):
        instructions = 'You are a helpful news curator. You summarize news articles. Change the text style according to the task. '
        if tone == 'simple':
            instructions += 'You use simple language and short sentences for children to understand.'
        elif tone == 'casual':
            instructions += 'You are friendly, lighthearted and excited!'
        return instructions

    @classmethod
    def length_str(cls, length: str):
        if length == 'short':
            return 'one-sentence'
        else:  # 'original'
            return 'one-paragraph'

    @classmethod
    def create_email_body(cls, output):
        text = ''
        for item in output:
            text += item['summary'] + '\n' + item['url'] + '\n\n'
        return text

    @classmethod
    def send_mail(cls, user_email: str, content):
        msg = EmailMessage()
        msg.set_content(content)

        msg['Subject'] = cls.config['GOODNEWS']['SUBJECT']
        msg['From'] = cls.config['GOODNEWS']['EMAIL']
        msg['To'] = user_email

        # Send message
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.ehlo()
        s.starttls()
        s.login(cls.config['GOODNEWS']['EMAIL'], cls.config['GOODNEWS']['EMAIL_PASS'])
        s.send_message(msg, cls.config['GOODNEWS']['EMAIL'], user_email)
        s.close()
        print(f"Email for {user_email}, has sent!")

    def app(self):
        _app = FastAPI()

        @_app.post('/create_and_send_newsletter')
        def create_and_send_newsletter(user_info: NewsRequestInput):
            newscollector = NewsCollector(sources=self.config['PATHS']['SOURCES'])
            collected_news_df = newscollector.scrape_news().sample(frac=1).reset_index(drop=True)  # Shuffles the df

            instructions = self.gpt_instructions(tone=user_info.tone)
            length = self.length_str(length=user_info.length)

            gpt_identify_uplift = GPTZeroShotClassification(classes=['Uplifting', 'Demoralizing', 'Neutral'])
            gpt_summarize = GPT(instructions=instructions)

            output = []
            for idx, row in collected_news_df.iterrows():
                if len(output) >= 6:
                    break
                if user_info.mode == 'Uplifting':
                    if gpt_identify_uplift.classify(row.body) != 'Uplifting':
                        continue
                d = {}
                d['url'] = row.url
                d['image_url'] = row.image_url
                gpt_summarize.add_message(row.body, user='user')
                d['summary'] = gpt_summarize("Write a {} summary of the article.".format(length)).text
                output.append(d)

            body_text = self.create_email_body(output)
            self.send_mail(user_info.email, body_text)

        return _app


def app():
    server = Server()
    return server.app()
