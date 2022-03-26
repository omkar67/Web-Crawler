import requests
from bs4 import BeautifulSoup
import pandas

l=[]
base_url="https://www.hp.com/in-en/shop/laptops-tablets.html?hp_facet_processortype=Intel+Core+i7&p="
for i in range(1,7):
    url=base_url+str(i)
    r=requests.get(url)
    c=r.content
    soup=BeautifulSoup(c,'html.parser')

    all=soup.find_all("div",{'class':"product details product-item-details"})
    print(len(all))
    for item in all:
        my_dict={}
        my_dict["Model Name"]=item.find('a',{'class':"product-item-link"}).text.strip()

        my_dict['Processor Infro']=item.find('li',{'class':'processorfamily'}).text

        nu=['Os','Display Infor']
        for x,y in zip(item.find_all('li',{'class':"osinstalled"}),nu):
            my_dict[y]=x.text

        
        
        try:
            my_dict["Graphics Capabilites"]=item.find('li',{'class':'graphicseg_01card_01-graphicseg_02card_01'}).text
        except:
            my_dict["Graphics Capabilites"]=None

        ram_harddisk=["RAM","Hard Disk Info"]
        for c,v in zip(item.find_all('li',{'class':'memstdes_01'}),ram_harddisk):
            my_dict[v]=c.text

        try:
            my_dict['Weight']=item.find('li',{'class':'weightmet'}).text
        except:
            my_dict['Weight']=None

        prices=["Max Price",'Disount Price','Curr Price']
        for j,h in zip(item.find_all('span',{'class':"price"}),prices):
            my_dict[h]=j.text
        l.append(my_dict)

df=pandas.DataFrame(l)
df.to_csv('output.csv')