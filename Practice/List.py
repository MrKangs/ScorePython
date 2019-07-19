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
