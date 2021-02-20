def fun(num):
    for i in range(num,0,-1):
        for j in range (0,i):
            print("*",end="")
        print()    


def main():
    print("enter the number")
    value=int(input())
    fun(value)
    
if __name__=="__main__":
    main()    