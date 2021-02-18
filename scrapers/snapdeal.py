def snapdeal(search):
    import requests as req
    from bs4 import BeautifulSoup
    from requests_html import HTMLSession
    initial_page='https://www.snapdeal.com/search?keyword='+search+'&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    session=HTMLSession()
    page=session.get(initial_page)
    page.html.render()
    soup=BeautifulSoup(page.html.raw_html,'html.parser')
    products = soup.select('div.product-tuple-listing')
    products_list=[]
    for x in products:
        details={}
        details['name']=(x.select_one('p.product-title').text)
        details['link']=(x.select_one('a.dp-widget-link')['href'])
        details['price']=float(x.select_one('span.product-price').text[3:])
        details['image']=(x.select_one('source')['srcset'])
        products_list.append(details)
    return products_list
