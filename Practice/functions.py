def cal_rec_area(x, y):
    return(x*y)

print(cal_rec_area(10,20))    



def spam(egg):
    egg.append(1)
    print(ham)
    egg=[2,3]
    print(egg)

ham=[0]
spam(ham)
print(ham)  

def math_fac(n):
    if n == 1: return(1)
    m=1
    for i in range(1,n):
        m=m*(i+1)
    return(m)

print(math_fac(5))





def swap_test(c,x,y):
    m = []
    b = c #[1,2,3,4,5] = [1,2,3,4,5]
    m = b
    temp=b[x]
    b[x]=b[y]
    b[y]=temp
    print(b, c, m) #My prediction: [1,3,2,4,5] [1,3,2,4,5] [1,2,3,4,5]

a = [1,2,3,4,5]
d=a
print(d)
swap_test(a,1,2)  
print(a, d) #My prediction: [1,3,2,4,5] [1,2,3,4,5]




def swap_test2(x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
    print(a)

a=[1,2,3,4,5]
c = []
#print(a) 
#swap_test2(1,2)
swap_test([1,2,3,4,5],1,2)
#print(a)  
#print(c) 

def test(t,z):
    temp = t
    t = z
    z = temp
    print(t,z)

x = 10
y = 50
print(x,y)
test(10,50)
print(x,y)

def f(s):
    s = "I love you"
    print(s)

s = "I love myself"
f(s)
print(s)