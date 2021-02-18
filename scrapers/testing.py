def flipkart(search):
    import requests as req
    from bs4 import BeautifulSoup
    import json
    initial_page='https://www.flipkart.com/search?q='+search+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    page = req.get(initial_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    products = soup.select('script')
    for x in products:
        if x.string is not None and 'window.__INITIAL_STATE__ ' in (x.string):
            y=json.loads(x.string.strip()[26:-1])
            for a in (y['pageDataV4']['page']['data']['ROOT'][1]['widget']['data']['renderableComponents']):
                print(a)




a=input()
flipkart(a)