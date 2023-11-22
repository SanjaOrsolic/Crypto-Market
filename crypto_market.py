from tkinter import*
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

URL="https://coinmarketcap.com/"
konekcija=requests.get(URL).content

podaci=BeautifulSoup(konekcija,"html.parser")

lista_price=[]

def grafikon():
    
    graf=plt.figure(figsize=(6,5.5))
    plt.title("Grafički prikaz cijena kriptovaluta")
    plt.xlabel("Naziv kriptovalute")
    plt.ylabel("Cijena kriptovalute")
    y=lista_price
    x=("Bitcoin", "Ethereum", "Tether", "BNB", "USD Coin")
    plt.bar(x, y,color=["#22577a","#38a3a5","#57cc99","#80ed99","#c7f9cc"])
    plt.show()

root=Tk()
root.title("Crypto Market")
root.config(bg="#0a9396")
root.geometry("400x550")

okvir1=Frame(root,width=400,height=100, bg="#005f73")
okvir1.place(x=0,y=0)

naslov=Label(okvir1, text="§ Crypto Market §", font=("MV Boli",18), fg="white",bg="#005f73")
naslov.place(x=80,y=30)

coin=Label(root,text="Coin",font=("MV Boli",14),bg="#0a9396")
coin.place(x=50,y=110)
price=Label(root,text="Price",font=("MV Boli",14),bg="#0a9396")
price.place(x=270,y=110)

#----Bitcoin okvir
okvir2=Frame(root, width=350,height=50)
okvir2.place(x=25,y=150)
bitcoin_logo=PhotoImage(file="bitcoin_logo.png").subsample(26)
slika_bitcoin=Label(okvir2, image=bitcoin_logo)
slika_bitcoin.place(x=0,y=0)
bitcoin=Label(okvir2, text="Bitcoin", font=("MV Boli",12))
bitcoin.place(x=60, y=10)

bitcoin_price_sup=podaci.select("#__next > div.sc-faa5ca00-1.cKgcaj.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-66133f36-2.cgmess > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > a > span")
print(bitcoin_price_sup)
bitcoin_price=(bitcoin_price_sup[0].text)
cisti1_b=bitcoin_price.strip().replace("$","")
cisti2_b=float(cisti1_b.strip().replace(",",""))

lista_price.append(cisti2_b)

bitcoin_pr=Label(okvir2, text=bitcoin_price, font=("Arial",12))
bitcoin_pr.place(x=230,y=10)


#----Ethereum okvir
okvir3=Frame(root, width=350,height=50)
okvir3.place(x=25,y=210)
ethereum_logo=PhotoImage(file="ethereum_logo.png").subsample(4)
slika_eth=Label(okvir3, image=ethereum_logo)
slika_eth.place(x=0,y=0)
eth=Label(okvir3, text="Ethereum", font=("MV Boli",12))
eth.place(x=60, y=10)

ethereum_price_sup=podaci.select("#__next > div.sc-faa5ca00-1.cKgcaj.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-66133f36-2.cgmess > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > a > span")
ethereum_price=(ethereum_price_sup[0].text)
cisti1_e=ethereum_price.strip().replace("$","")
cisti2_e=float(cisti1_e.strip().replace(",",""))
lista_price.append(cisti2_e)

eth_pr=Label(okvir3, text=ethereum_price, font=("Arial",12))
eth_pr.place(x=230,y=10)

#---- Tether okvir
okvir4=Frame(root, width=350,height=50)
okvir4.place(x=25,y=270)

tether_logo=PhotoImage(file="tether_logo.png").subsample(4)
slika_teth=Label(okvir4, image=tether_logo)
slika_teth.place(x=0,y=0)
teth=Label(okvir4, text="Tether", font=("MV Boli",12))
teth.place(x=60, y=10)

tether_price_sup=podaci.select("#__next > div.sc-faa5ca00-1.cKgcaj.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-66133f36-2.cgmess > table > tbody > tr:nth-child(3) > td:nth-child(4) > div > a > span")
tether_price=(tether_price_sup[0].text)
cisti1_t=tether_price.strip().replace("$","")
cisti2_t=float(cisti1_t.strip().replace(",",""))
lista_price.append(cisti2_t)

teth_pr=Label(okvir4, text=tether_price, font=("Arial",12))
teth_pr.place(x=230,y=10)

#---- BNB okvir
okvir5=Frame(root, width=350,height=50)
okvir5.place(x=25,y=330)
BNB_logo=PhotoImage(file="BNB_logo.png").subsample(42)
slika_BNB=Label(okvir5, image=BNB_logo)
slika_BNB.place(x=0,y=0)
BNB=Label(okvir5, text="BNB", font=("MV Boli",12))
BNB.place(x=60, y=10)

BNB_price_sup=podaci.select("#__next > div.sc-faa5ca00-1.cKgcaj.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-66133f36-2.cgmess > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > a > span")
BNB_price=(BNB_price_sup[0].text)
cisti1_bnb=BNB_price.strip().replace("$","")
cisti2_bnb=float(cisti1_bnb.strip().replace(",",""))
lista_price.append(cisti2_bnb)

BNB_pr=Label(okvir5, text=BNB_price, font=("Arial",12))
BNB_pr.place(x=230,y=10)


#---- USD Coin okvir
okvir6=Frame(root, width=350,height=50)
okvir6.place(x=25,y=390)
USD_logo=PhotoImage(file="USD_coin_logo.png").subsample(4)
slika_USD=Label(okvir6, image=USD_logo)
slika_USD.place(x=0,y=0)
USD=Label(okvir6, text="USD Coin", font=("MV Boli",12))
USD.place(x=60, y=10)

USD_price_sup=podaci.select("#__next > div.sc-faa5ca00-1.cKgcaj.global-layout-v2 > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-66133f36-2.cgmess > table > tbody > tr:nth-child(6) > td:nth-child(4) > div > a > span")
USD_price=(USD_price_sup[0].text)
cisti1_u=USD_price.strip().replace("$","")
cisti2_u=float(cisti1_u.strip().replace(",",""))
lista_price.append(cisti2_u)

USD_pr=Label(okvir6, text=USD_price, font=("Arial",12))
USD_pr.place(x=230,y=10)



gumb=Button(root, text="Grafički prikaz", font=("MV Boli",18), fg="white",bg="#005f73", command=grafikon)
gumb.place(x=90, y=470)






root.mainloop()