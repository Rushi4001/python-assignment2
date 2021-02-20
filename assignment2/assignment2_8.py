def fun(num):
    for i in range(num,):
        for j in range (i+1):
            print(j+1,end="")
        print()    


def main():
    print("enter the number")
    value=int(input())
    fun(value)
    
if __name__=="__main__":
    main()    