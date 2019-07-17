
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_2?keywords=gopro&qid=1562880420&s=amazon-devices&sr=8-2'
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

#title = soup.find(id = "productTitle").get_text()
#print(title, strip())
