from __future__ import annotations

from fastapi import FastAPI

from curator import CuratorBase, NewsCollector


class Server(CuratorBase):
    def __init__(self, sources):
        super().__init__()
        self.newscollector = NewsCollector(sources=sources)
        self.news_df = None
        self.featured_clusters = None

    def app(self):
        _app = FastAPI()

        @_app.post('/retrieve_news')
        def retrieve_news():
            self.news_df = self.newscollector.scrape_news()

        @_app.post('/cluster_news')
        def cluster_news():
            self.featured_clusters = self.newscollector.cluster_news(news_df=self.news_df)

        return _app


def app():
    server = Server()
    return server.app()
