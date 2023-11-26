import argparse

from curator.backend import Client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, nargs='?', default='http://localhost:8080/')
    opt = parser.parse_args()

    client = Client(host=opt.host)

    news_df = client.retrieve_news()
    print(news_df)

    clusters = client.cluster_news()
    print(clusters)


if __name__ == '__main__':
    main()
