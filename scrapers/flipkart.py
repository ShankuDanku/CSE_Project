def flipkart(search):
    import requests as req
    from bs4 import BeautifulSoup
    from requests_html import HTMLSession
    initial_page='https://www.flipkart.com/search?q='+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    session=HTMLSession()
    page=session.get(initial_page)
    page.html.render()
    soup = BeautifulSoup(page.html.raw_html, 'html.parser')
    products = soup.select('div a')
    print(products)
a=input()
flipkart(a)