import fake_useragent

URL = 'http://neva-basket.ru/teams/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
USER = fake_useragent.UserAgent().random

HEADERS = {
    'User-Agent': USER
}