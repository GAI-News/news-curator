from curator import Config, NewsCollector


config = Config()
newscollector = NewsCollector(sources=config['PATHS']['SOURCES'])

news_df = newscollector.scrape_news()
newscollector.cluster_news(news_df=news_df)
