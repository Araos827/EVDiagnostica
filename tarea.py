import json

with open("farmers-protest-tweets-2021-03-5.json", "r", encoding='utf-8', errors='replace') as file:
    tweets = [json.loads(line) for line in file]
    file.close()

def f1():
    lista1 = (sorted(tweets, key = lambda i: i["retweetCount"],reverse=True))
    lista1 = lista1[0:10]
    for element in lista1:
        print(element["content"] + "\n")

def f2():
    lista_aux = []
    most_common = list()
    for line in tweets:
        lista_aux.append(line["user"]["username"])
    users_counter = collections.Counter(lista_aux)
    most_common = users_counter.most_common(10)
    for user in most_common:
        print(user[0] + "\n")
        
def f3():
    lista_aux = []
    most_days = list()
    for line in tweets:
        lista_aux.append(line["date"][0:10])
    counter = collections.Counter(lista_aux)
    most_days = counter.most_common(10)
    for date in most_days:
        print(date[0], "\n")

def f4():
    lista_aux = []
    most_common = list()
    for line in tweets:
        frase = line["content"].split()
        for palabra in frase:
            if palabra[0] == "#":
                lista_aux.append(palabra)
    counter = collections.Counter(lista_aux)
    most_common = counter.most_common(10)
    for hashtag in most_common:
        print(hashtag[0] + "\n")

if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    pass