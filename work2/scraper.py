
from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_2?keywords=gopro&qid=1562880420&s=amazon-devices&sr=8-2'
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup = BeautifulSoup(soup1.prettify(), 'html.parser')

    #print(soup.prettify())
    title = soup.find(id="productTitle").text  #get_text
    price = soup.find(id="priceblock_ourprice").text    #$330.00
    convert_price=float(price.split('$')[1])

    if (convert_price < 350.00):
      send_mail()

    print(title.strip())     # GoPro HERO 7 Black
    print(convert_price)

def send_mail():


    subject = 'Price Fell Down !'
    body = 'Check Amazon link: https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/dp/B07GDGZCCH/ref=sr_1_2?keywords=gopro&qid=1562880420&s=amazon-devices&sr=8-2 '
    msg = f" Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com','587')  # make sure set less security on email security setting
        server.set_debuglevel(debuglevel)
        server.ehlo()
        server.starttls()
        print('starttls OK !')
        server.login('bigsql@yahoo.com', 'moon13131414yaho')
        print('login OK !')
        server.sendmail('big@yahoo.com','bwhale1@yahoo.com',msg)
        print('An email has been sent !')
        server.quit()
    except:
        print ('can\'t send the Email')


if __name__ == "__main__":
    check_price()
