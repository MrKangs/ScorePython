print("안녕하세요! 데이터 활용 세상입니다!")

color1=["red","yellow","green"]
color2=["black","blue","orange","skyblue"]

total_color=color1+color2

print(color1)
print(total_color[::2])
print(total_color[::-1])

color1.append("white")
print(color1)
total_color=color1+color2
print(total_color)

a=[1,2,3,4,5]
b=[9,7,5,3,1,7,4,6,0]
print(a)
print(b)
c=a+b
print(c)

b.sort()
print(b)

d=[1,2,3]
x,y,z=d
print(d)
print(x,y,z)

a=[1,2,3,4,5]
b=[0,9,8,7,6]
ab=[a,b]
print(ab)
print(ab[0][2])


sentence="ILoveYou"
r_sentence=""
for char in sentence:
    r_sentence =char+r_sentence
    print(r_sentence) 

print("당신이 원하는 구구단을 입력하세요")
u_input=int(input())
print("당신이 원하는",u_input," 단은 다음과 같습니다")
for i in range(1,10):
    print(u_input,"X",i,"=",u_input*i)


math_data=[12,43,56,78,90,99,87,65,46,34,66,77,88,44,99,77,56]
num_end=int(len(math_data))
for i in range(0,num_end):
    if (math_data[i]) >= 90: print("Grade A")
    elif (math_data[i]) >= 80: print("Grade B") 
    elif (math_data[i]) >= 70: print("Grade C")
    elif (math_data[i]) >= 60: print("Grade D")
    else: print("Grade F")                