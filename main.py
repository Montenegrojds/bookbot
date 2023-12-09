with open("books/frankenstein.txt") as f:
    file_contents = f.read()
#print(file_contents)   
words = file_contents.split()
print(type(words))
dic = {}
for x in words:
    palabra = x.lower()
    for letra in palabra:
        dic[letra] = dic.get(letra,0)+1

for y in dic:
    print ("The '"+y+" character was found "+str(dic[y])+" times") 