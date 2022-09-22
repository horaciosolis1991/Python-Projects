import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import date

data=pd.DataFrame(columns=['elemento', 'descuento', 'marca','genero'])
start_time = time.time()
page = requests.get("https://simple.ripley.cl/moda-hombre/destacados/todo-moda-hombre?m-moda-hombre-vertodo=&s=mdco")
soup    = BeautifulSoup(page.content, 'html.parser')
withtag=soup.find_all("div", {"class": "catalog-product-item catalog-product-item--moda catalog-product-item__container col-xs-6 col-sm-6 col-md-4 col-lg-4"})
for i in range(len(withtag)):
        #print(withtag[i].find('a').get('href')) #concatenation with simple.ripley.... is needed.
        #print( withtag['i'].find("div",{"class","catalog-product-details__logo-container"}))
    try:
        if withtag[i].find("div", {"class": "catalog-product-details__discount-tag"}).get_text():
            data=data.append({'elemento':'https://simple.ripley.cl'+withtag[i].find('a').get('href'),'descuento':withtag[i].find("div", {"class": "catalog-product-details__discount-tag"}).get_text().replace('-',''),
                                              'marca':withtag[i].find("div",{"class","brand-logo"}).find('span').get_text(),'genero':'hombre'}, ignore_index=True)
                #print( withtag[i].find("div",{"class","brand-logo"}).find('span').get_text())
                #print(withtag[i].find("div", {"class": "catalog-product-details__discount-tag"}).get_text().replace('-',''),i)
                # PRECIO NORMAL FUNCIONANDO ---> print(withtag[i].find("li", {"class": "catalog-prices__list-price catalog-prices__lowest catalog-prices__line_thru"}).get_text())
    except:
        continue
print("--- %s seconds ---" % (time.time() - start_time)) 
now = date.today()
current_time = now.strftime("%d/%m/%Y").replace('/','_')
data.to_excel('ripleyh'+current_time+'.xlsx')     