import argparse

from curator import Config
from curator.backend import Client, NewsRequestInput


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, nargs='?', default='http://localhost:8080/')
    opt = parser.parse_args()

    config = Config()
    client = Client(host=opt.host)

    user_info = NewsRequestInput(
        email=config['USER']['EMAIL'],  # user@gmail.com
        mode=config['USER']['MODE'],  # uplifting
        tone=config['USER']['TONE'],  # simple
        length=config['USER']['LENGTH']  # short
    )
    client.create_and_send_newsletter(user_info=user_info)


if __name__ == '__main__':
    main()
