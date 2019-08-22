def cal_rec_area(width, length):    # width and length are called parameter
    return(width*length)

print(cal_rec_area(10,20)) # call function and print the result from the return value with arguments 10 and 20 
#######################################################################################

def Add(num1,num2):
    print("{0}+{1}={2}".format(num1,num2,num1+num2)) 
    print("{1}+{0}={2}".format(num1,num2,num1+num2)) 

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
    print(ham)  #egg == ham and egg is changed then egg will be [0 1]=egg=ham
    print(egg)
    egg=[2,3]   # egg is assigned by [2, 3] then egg=[2, 3] not equal ham=[0,1]
    print(egg)
    print(ham)

ham=[0]
spam(ham)
print(ham) 
#####################################################################################

print("Factorial Calculation")
def math_fac(n):              # factorial of n
    if n == 1: return(1)
    m=1
    for i in range(1,n):
        m=m*(i+1)
    return(m)

print(math_fac(5))


print("Recursive Function with same result")
def math_fac2(n):
    if n == 1: 
            return(1)
    else:
            return(n*math_fac2(n-1))

print(math_fac2(5))

####################################################################################



print("This is for test of swap-test")
def swap_test(c,x,y):
    m=list(c)  # m is newly assigned by list(c). Hence  m = [1,2,3,4,5] 
    temp=c[x]
    c[x]=c[y]
    c[y]=temp  # c is changed. Hence c will be changed. and c=a=[1,3,2,4,5]
    print(m)
    print(c) 

a = [1,2,3,4,5]
swap_test(a,1,2)  
print(a)  # but print(c) will be error of value.
# Please see https://www.youtube.com/watch?v=0ccHFT0-8bg&list=PLBHVuYlKEkUJcXrgVu-bFx-One095BJ8I&index=31 from 3:03



print("This is for test of swap-test2")
def swap_test2(x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp # a was changed and hence the a will be changed.
    print(a)

a=[1,2,3,4,5]
c = []
print(a) 
swap_test2(1,2)
#swap_test([1,2,3,4,5],1,2)
print(a)  
print(c) 

########################################################################

print("This is for test of swap-test3")
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

print("This is for test of swap-test4")
def f(a):
    print(a)
    a = "I love you" # a is assigned by "I love you"(new value) Hence a = I love you and s will not be changed.
    print(a)

s = "I love myself"
f(s)
print(s)




print("This is for test of swap-test5 with global value")
def f():
    global s    
    print(s)
    s = "I love you" # a is assigned by "I love you"(new value) Hence a = I love you and s will not be changed.
    print(s)

s = "I love myself"
f()
print(s)

 
#########################################################################
print("Using Asterisk ###############################")
def asterisk_test(a,b,*args):
        print("The first vale {} and second value {}".format(a,b))
        print(args) #tuple type 
        return a+b+sum(args)

print(asterisk_test(1,2,3,4,5,10))

print("Unpacking Asterisk")
def asterisk_test2(*args):
        x,y,z,a,b,c = args
        print("The first vale {} and second value {}".format(x,y))
        print(args) #tuple type 
        return sum(args)

print(asterisk_test2(111,222,3,4,5,10))


def asterisk_test3(*args):
        x,y,*z = args
        print("The first vale {} and second value {}".format(x,y))
        print(args,z) #tuple type 
        return sum(z)

print(asterisk_test3(111,222,3,4,5,10))


def asterisk_test4(**kwargs):
        print(kwargs)
        print("Print {second} and {first}".format(**kwargs))
        print(kwargs["first"], "and ", kwargs["second"])

asterisk_test4(first=111,second=222)
 