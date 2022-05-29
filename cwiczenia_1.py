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

#%%

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

if len(list1)>=len(list2):
    lista_dluga= len(list1)
    lista_krotka = len(lista2)
    list1=list1
    list2=list2
else: 
    lista_dluga=len(list2)
    lista_krotka= len(list1)
    list1=list2
    list2=list1
for i in range (lista_krotka):
    for j in range(lista_dluga):
        if list1[i]==list2[j]:
            print("True")
    break
    print("False")
    
    
for item1 in list1:
    if item1 in list2:
        result = True
        break
 
print(result)
print(type('dupa'))
        
#%%        
hashtags = ['holiday', 'sport', 12,'fit', 'fashion']
result=True
for i in hashtags:
    if not isinstance(i, str):
        result = False
        break
    
print(result)

#%%
number = 2

def pierwsza(number):
    liczba_pierwsza = True
    for i in range(2,number+1):
        dzielnik = i
        if number % dzielnik == 0:
            liczba_pierwsza = False
            break
            return False
        else: 
            print(f"{number} - liczba pierwsza")
            return 
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - nie jest pierwsza')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} - nie jest pierwsza')
            
#%%
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}   

def waluta(slownik):
    for key, value  in slownik.items():
        if value[1] =='USD':
            value[0]= value[0]*4.0
            value[1] = "PLN"
    print(slownik)
                

waluta(gaming)

for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] * 4.0
    info[1] = 'PLN'
print(gaming)

#%%
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for i in names:
    if i == None:
        continue
    print(i)
    
#%%

licznik = 10
while r <=10:
    for i in range(2,100):
        for j in range(i:2:-1)

#%%
#lambda <parametry> : <wyrażenie>
stocks = ['playway', 'boombit', 'cd projekt']

print(list(map(lambda x : len(x),stocks)))

#%%
def sort_list(lista):
    dupa = lambda x: sorted(x[1])
    return dupa

print(sort_list([('h','b'), ('z','a'), ('w','c')]))


#%%
def sort_list(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i][1] > lista[j][1]
        
            

dupa = sort_list([('h','b'), ('z','a'), ('w','c')])
print(dupa)
                
        




