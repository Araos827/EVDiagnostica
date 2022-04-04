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
        
if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    
    pass