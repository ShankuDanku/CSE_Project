def ebay(search):
    import requests as req
    from bs4 import BeautifulSoup


    initial_page='https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+search+'&_sacat=0'
    page=req.get(initial_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    products = soup.select('#mainContent li')
    products_list=[]
    for product in products:
        details={}
        if product.select_one('a h3') is not None:
            details['site']='EBAY'
            details['name']=(product.select_one('a h3').text)
            details['price']=(product.select_one('.s-item__price').text)
            details['price']=details['price'].replace(',','')
            if 'to' in details['price']:
                xyz=details['price'].split()
                details['price']=round((float(xyz[0][1:])+float(xyz[2][1:]))/2*72.81,2)
            else:
                details['price']=round(float(details['price'][1:])*72.81,2)
            details['image']=(product.select_one('.s-item__image-img')['src'])
            if (product.select_one('a')) is not None:
                details['link']=(product.select_one('a')['href'])
            if details not in products_list:
               products_list.append(details)
    return products_list

    #print(soup.select_one('.pagination__next')['href'])