from bs4 import BeautifulSoup
import requests

class MusicService:
    def __init__(self):
        self.url = "https://smu.melon.com/chart/index.htm#"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.melon.com/chart/index.htm",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        self.class_name = []

    async def get_melon_chart(self):
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text, "html.parser")

        ls = soup.find_all("div", class_="ellipsis rank01")

        print("🕷️🕷️🕷️🕷️⚛️⚛️⚛️⚛️멜론 차트 크롤링 완료🍇🍇🍇🍇🍇")

        for i in ls:
            print(i.text)


        
        return soup

