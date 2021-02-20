def fun(num):
    for i in range (1,num+1,1):
        for j in range(1,num+1,1):
            print(j,end="")
        print()
def main():
    print("enter the number")
    value=int(input())
    fun(value)
    


if __name__ == "__main__":
    main()