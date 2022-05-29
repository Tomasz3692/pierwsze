def sumka_cyfr(n):
    assert n>=0 and int(n)==n , "Błąd nie dałeś czałkowitej dodatniej"
    if n == 0:
        return 0

    else:
        return int(n%10) + sumka_cyfr(int(n//10))

print(sumka_cyfr(-124))

#%%
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

print(capitals.get('Austria'))

#%%
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

print(stocks.get('PLW')) = text.split(' ')
print(stocks['PLW'])

#%%
text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
text= text.split(' ')
x = " ".join(text)
x.split(' ')
x=list(x)
print(x)
print(type(x))

    

#print(text)
#.replace("\n", " ")
#print(dupa)

    
#%%




text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""

x = text.split()
y=[]
for i in range(len(x)):
    dupa = x[i].lower().replace(',','')
    if dupa.isalpha() and len(dupa)>10:
        
        y.append(dupa)
print(y)

#%%
import re
indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE', 
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
]


dwa = '20'
trzy = '30'
for i in range(len(indexes)):
    dupa = indexes[i]
    if dwa  in dupa:
        print(dupa)
    if trzy  in dupa:
        print(dupa)
        
        
for index in indexes:
    if '20' in index or '30' in index:
        print(index)
        
#%%

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for key, value in gaming.items():
    if value > 100:
        print(key)
        
#%%    
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']  
for i in names:
    if i.isalpha():
        print(f"Hello {i}!")
        
#%%
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]




