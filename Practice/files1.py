# r(read), w(write), a(append)
with open("D:\\Python\\ScorePython\\ace.txt", "r") as f: # the f is called a file point(handler)
    print(f.read())

g=open("D:\\Python\\ScorePython\\ace.txt", "r")
print(g.read())
f.close()
############################################################


with open("D:\\Python\\ScorePython\\out.txt", "a") as f:
    f.write("Python is good. \n")
    f.write("Python is more good. \n")
    f.write("Python is most good. \n")


with open("D:\\Python\\ScorePython\\out.txt", "r") as f: # the f is called a file point(handler)
    print(f.read())
