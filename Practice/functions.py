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