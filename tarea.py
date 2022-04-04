import json

with open("farmers-protest-tweets-2021-03-5.json", "r", encoding='utf-8', errors='replace') as file:
    tweets = [json.loads(line) for line in file]
    file.close()

def f1():
    lista1 = (sorted(tweets, key = lambda i: i["retweetCount"],reverse=True))
    lista1 = lista1[0:10]
    for element in lista1:
        print(element["content"] + "\n")

if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    
    pass