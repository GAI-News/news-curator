from thirdparty.newscollector.newscollector import NewsCollector
from curator import Config

config = Config()

newscollector = NewsCollector(
    sources=config['PATHS']['SOURCES'],
    template=config['PATHS']['HTML_TEMPLATE']
)
newscollector.create()
