def cal_rec_area(width, length):    # width and length are called parameter
    return(width*length)

print(cal_rec_area(10,20)) # call function and print the result from the return value with arguments 10 and 20 
#######################################################################################

def Add(num1,num2):
    print("{}+{}={}".format(num1,num2,num1+num2)) 

Add(10,20)    
#####################################################################################

def Add2(x,*y):
    print("x=",x)
    for i in y:
        print(i, end=' ')
        print(i)

Add2(1,2,3,4,5)        
#####################################################################################


def spam(egg):
    egg.append(1)
    print(ham)
    egg=[2,3]
    print(egg)

ham=[0]
spam(ham)
print(ham)  
#####################################################################################


def math_fac(n):              # factorial of n
    if n == 1: return(1)
    m=1
    for i in range(1,n):
        m=m*(i+1)
    return(m)

print(math_fac(5))
####################################################################################




def swap_test(c,x,y):
    m=list(c)   
    temp=c[x]
    c[x]=c[y]
    c[y]=temp
    print(m)
    print(c) #My prediction: [1,3,2,4,5] [1,3,2,4,5] [1,2,3,4,5]

a = [1,2,3,4,5]
swap_test(a,1,2)  
print(a) #My prediction: [1,3,2,4,5] [1,2,3,4,5]




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
#########################################################################


def f(s):
    s = "I love you"
    print(s)

s = "I love myself"
f(s)
print(s)