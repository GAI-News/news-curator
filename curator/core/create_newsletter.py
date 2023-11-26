from curator import GPT
from curator import GPTZeroShotClassification
from curator import NewsCollector
from curator import Config
import pandas as pd
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication

config = Config()

newscollector = NewsCollector(
    sources=config['PATHS']['SOURCES']
)
collected_news_df = newscollector.scrape_news().sample(frac=1).reset_index(drop=True) # Shuffles the df

# User configurable parameters
PARAMS = {
    'mode': 'uplifting', # can be neutral, uplifting, demoralizing
    'tone': 'simple', # can be simple, casual, academic
    'length': 'short', # short or original
    'email': "re.bekled@gmail.com"
}

instructions = 'You are a helpful news curator. You summarize news articles. Change the text style according to the task. '
if PARAMS['tone'] == "simple":
    instructions += 'You use simple language and short sentences for children to understand.'
if PARAMS['tone'] == "casual":
    instructions += 'You are friendly, lighthearted and excited!'
if PARAMS['length'] == "short":
    length = 'one-sentence'
else:
    length = 'one-paragraph'

gpt_identify_uplift = GPTZeroShotClassification(classes=['Uplifting', 'Demoralizing', 'Neutral'])
gpt_summarize = GPT(instructions=instructions)

output = []
for idx, row in collected_news_df.iterrows():
    if len(output) >= 6:
        break
    if PARAMS['mode'] == 'Uplifting':
        if gpt_identify_uplift.classify(row.body) != 'Uplifting':
            continue
    d = {}
    d['url'] = row.url
    d['image_url'] = row.image_url
    gpt_summarize.add_message(row.body, user='user')
    d['summary'] = gpt_summarize("Write a {} summary of the article.".format(length)).text
    output.append(d)

# This is where we send an email
SUBJECT = 'Your GoodNews!'
EMAIL_USER = 'goodnews.seoultechimpact@gmail.com'
EMAIL_PASS = 'vplcbqstyyveldkh'
EMAIL_RECEIVER = PARAMS['email']

def create_email_body(output):
    text = ''
    for item in output:
        text += item['summary'] + '\n' + item['url'] + '\n\n'
    return text

def send_mail(EMAIL_RECEIVER, BODY_TEXT):
    msg = EmailMessage()
    msg.set_content(BODY_TEXT)

    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_RECEIVER

    #Send message
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()
    s.starttls()
    s.login(EMAIL_USER, EMAIL_PASS)
    s.send_message(msg, EMAIL_USER,EMAIL_RECEIVER)
    s.close()
    print(f"Email for {EMAIL_RECEIVER}, has sent!")

BODY_TEXT = create_email_body(output)
send_mail(EMAIL_RECEIVER, BODY_TEXT)