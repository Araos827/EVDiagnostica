import json

with open("farmers-protest-tweets-2021-03-5.json", "r", encoding='utf-8', errors='replace') as file:
    tweets = [json.loads(line) for line in file]
    file.close()

if __name__ == '__main__':
    #f1()
    #f2()
    #f3()
    #f4()
    
    pass