def swap_test(c,x,y):
    m=list(c) 
    n = c
    temp=c[x]
    c[x]=c[y]
    c[y]=temp
    print(m,n,c) #My prediction: [1,2,3,4,5] [1,2,3,4,5] [1,3,2,4,5] 

a = [1,2,3,4,5]
d = a
swap_test(a,1,2)  
print(a, d) #My prediction: [1,3,2,4,5] [1,2,3,4,5]


 
#def swap_int(x,y):
#    temp = x
#    x = y
#    y = temp
#    print(x,y)
#
#A = 10
#B = 20
#C = A
#print(A,B,C)
#swap_int(A,B)
#print(A,B,C)