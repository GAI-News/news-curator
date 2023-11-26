from datetime import datetime, date

from thirdparty.newscollector.newscollector import Helper, Scraper, Processer
from curator import CuratorBase


class NewsCollector(CuratorBase):
    def __init__(self, sources, news_date=date.today()):
        super().__init__()
        self.sources = Helper.load_sources(sources)
        self.news_date, self.day_before = Helper.validate_date(news_date)

    def scrape_news(self):
        start = datetime.now()
        scraper = Scraper(self.sources, news_date=self.news_date)
        self.sources = scraper.scrape()

        news_df = Helper.write_dataframe(self.sources)
        end = datetime.now()
        Helper.print_scrape_result(news_df, start, end)

        news_df = Helper.clean_dataframe(news_df)
        news_df = Helper.clean_articles(news_df)

        return news_df

    def cluster_news(self, news_df):
        tfidf_df = Processer.compute_tfidf(news_df)
        clusters = Processer.find_clusters(news_df, tfidf_df)
        featured_clusters = Processer.find_featured_clusters(clusters)

        return featured_clusters
