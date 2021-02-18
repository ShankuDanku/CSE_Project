import ebay,ajio,snapdeal,Amazon
def call(search):
    a= Amazon.amazon(search)
    b= ajio.ajio(search)
    c= ebay.ebay(search)
    d= snapdeal.snapdeal(search)
    a.extend(b)
    a.extend(c)
    a.extend(d)
    print(a)
call(search='shoe')

