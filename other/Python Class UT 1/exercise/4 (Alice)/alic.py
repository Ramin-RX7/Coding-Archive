def last_elem(x):
    return x[1]
my_dict={}
my_file= open('alice.txt', mode='r')
content= my_file.read()
content= content.lower()
words= content.split()
for word in words:
    if word in my_dict.keys():
        my_dict[word] = my_dict[word] + 1
    else:
        my_dict[word] = 1


words= my_dict.keys()
sorted_words= sorted(words)
sorted_items= sorted(my_dict.items(), key=last_elem, reverse= True)
for word, num in sorted_items:
    print(word+ ': '+ str(num))
