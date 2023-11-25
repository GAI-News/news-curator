from curator import GPT
from thirdparty.newscollector.newscollector import NewsCollector
from curator import Config
import pandas as pd
import json

config = Config()

newscollector = NewsCollector(
    sources=config['PATHS']['SOURCES'],
    output_filename='resources/newsletter_input.csv',
    news_date='2023-11-24'
)
newscollector.create()

collected_news_df = pd.read_csv('resources/newsletter_input.csv').dropna()

uplifting = True
# User configurable

gpt_identify_uplift = GPT(instructions='You are a helpful news curator. Is this article more uplifting or more demoralizing? Say only 1 word. No explanation needed.')
gpt_summarize = GPT(instructions='You are a helpful news curator. You summarize news articles. Change the text style according to the task. You use simple language and short sentences for children to understand. You are friendly, lighthearted and excited!')

output = []
for idx, row in collected_news_df.iterrows():
    if len(output) >= 6:
        break
    if uplifting:
        if gpt_identify_uplift(row.body).text != 'Uplifting':
            continue
    d = {}
    d['url'] = row.url
    d['image'] = row.image
    gpt_summarize.add_message(row.body)
    d['summary'] = gpt_summarize("Write a one-sentence summary of the article.").text
    output.append(d)

with open('resources/newsletter_output.jsonl', 'w') as f:
    for item in output:
        f.write(json.dumps(item) + '\n')