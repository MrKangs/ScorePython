def main():
    f = open("Score.txt", "w+") #새로운 파일을 열고 이 프로그렘이 쓸 수 있는 권한을 주는 프로그램. 
    #Window 10이면 Microsfot에서 Python를 다운 받아야 한다. 이미 있는데도... ㅠㅠ

    for i in range(10):
        f.write("This is line " + str(i+1) + "\r\n")
    
    f.close() #파일을 닫는다

    f = open("Score.txt", "r") # r는 읽기 모드
    if f.mode == 'r': 
        #Method 1
        contents = f.read() #read() function는 그 내용을 복사는 형식
        print (contents)
        #Method 2
        fl = f.readlines()#readlines() function는 줄 한개씩 읽는 용도(복사까지)
        for x in fl:
            print(x)

# https://code.tutsplus.com/tutorials/how-to-work-with-excel-documents-using-python--cms-25698 (English)
#https://doitnow-man.tistory.com/159(한국어 #1)
#https://myjamong.tistory.com/51 (한국어 #2)
#https://pinkwink.kr/959 (한국어 #3 with graphs)
#Need to look into this to interact with Excel 
if __name__ == "__main__":
    main()