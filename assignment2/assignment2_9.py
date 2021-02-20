def fun(num):
    count=0
    while num>0:
        count=count+1
        num=num//10
    print("the number of digit in the number are",count)
    
    
    
def main():
    print("enter the number")
    value=int(input())
    fun(value)
    


if __name__ == "__main__":
    main()