def fun(num):
    x=1
    sum=0
    while x<=num:
        if num%x==0:
            sum=sum+x
        x=x+1
    print(sum)
    
def main():
    print("enter the number ")
    value=int(input())
    
    fun(value)
    
if __name__=="__main__":
    main()