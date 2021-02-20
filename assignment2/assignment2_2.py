def fun(num):
    x=1
    while x<num:
        print("*"*num)
        x=x+1

def main():
    print("enter the number")
    value=int(input())
    fun(value)
    


if __name__ == "__main__":
    main()