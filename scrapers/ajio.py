def ajio(search):
    import requests as req
    from bs4 import BeautifulSoup
    from requests_html import HTMLSession
    import json

    initial_page = 'https://www.ajio.com/search/?text=' + search
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page = req.get(initial_page,headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    products=soup.select('script')
    product_list=[]
    for x in products:
        if x.string is not None and 'window.__PRELOADED_STATE__' in x.string:
           y=json.loads(x.string.strip()[29:-1])
           for a in y['grid']['entities']:
               details={}
               details['site']='AJIO'
               details['name']=(y['grid']['entities'][a]['name'])
               details['image']=(y['grid']['entities'][a]['fnlColorVariantData']['outfitPictureURL'])
               details['price']=float(y['grid']['entities'][a]['price']['value'])
               details['link']=('https://www.ajio.com'+y['grid']['entities'][a]['url'])
               if details not in product_list:
                  product_list.append(details)
    return product_list
