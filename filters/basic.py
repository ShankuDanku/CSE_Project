def minmax(product_list, minprice=0, maxprice=None):
    minmaxlist = []
    if maxprice == None:
        for product in product_list:
            if int(product['price']) >= minprice:
                minmaxlist.append(product)
    else:
        for product in product_list:
            if (product['price']) >= minprice and product['price'] <= maxprice:
                minmaxlist.append(product)
    return minmaxlist


def sortascending(product_list):
    sortdlst=[]
    while product_list!=[]:
        minimum=product_list[0]['price']
        count=product_list[0]
        for x in product_list:
            if minimum>x['price']:
                minimum=x['price']
                count=x
        sortdlst.append(count)
        product_list.remove(count)
    return sortdlst

def misc(product_list,miscellaneous):
    misc_list=[]
    for x in product_list:
        if miscellaneous.lower() in x['name'].lower():
            misc_list.append(x)
    return misc_list


