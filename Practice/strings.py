a="DongSeungKang"
b="KennethKang"

print(len(a))
print(a.upper())
print(b.lower())

print(a[::2]+" "+b[::-2])
print(a[2:4])

print("The number of ng in the string "+a+" has",a.count("ng"))



x=[1,2,3,4,5]
x.append(10)
x.append(20)
print(x)
print(x,x.pop())

word = input("Input a word : ")
word_list = list(word)

for i in range(len(word_list)):
    print(word_list.pop())