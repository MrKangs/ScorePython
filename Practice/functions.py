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


def swap_test(b,x,y):
    c = b
    temp=b[x]
    b[x]=b[y]
    b[y]=temp
    print(c)

a=[1,2,3,4,5]
print(a) 
swap_test(a,1,2)
print(a)   

def test(t,z):
    temp = t
    t = z
    z = temp
    print(t,z)

x = 10
y = 50
print(x,y)
test(x,y)
print(x,y)