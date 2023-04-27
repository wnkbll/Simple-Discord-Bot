from src.client import Client
from src.config import settings


def main():
    bot = Client()
    bot.run(settings['token'])


if __name__ == '__main__':
    main()
