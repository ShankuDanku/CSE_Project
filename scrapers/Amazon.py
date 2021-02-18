def amazon(search):
    import requests as req
    from bs4 import BeautifulSoup

    initial_page='https://www.amazon.in/s?k='+search
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page=req.get(initial_page,headers=headers)
    soup=BeautifulSoup(page.text,'html.parser')
    products = soup.select('div.s-result-item')
    product_list=[]
    for product in products:
        details={}
        try:
            details['site']='AMAZON'
            details['name']=(product.select_one('h2 a.a-link-normal span').text)
            details['link']=('https://www.amazon.in'+product.select_one('h2 a.a-link-normal')['href'])
            details['price']=float((product.select_one('span.a-price-whole').text).replace(',',''))
        except:
            continue
        try:
            details['image']=(product.select_one('img.s-image')['src'])
        except:
            details['image']=''
        if details not in product_list:
           product_list.append(details)
    return (product_list)
