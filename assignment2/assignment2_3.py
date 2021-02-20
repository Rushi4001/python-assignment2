def fun(num):
    fac=1
    while num>0:
        fac=fac*num
        num=num-1
    print("factorial is:",fac)
    
    
def main():
    value=int(input("enter the number"))
    
    fun(value)
    
if __name__=="__main__":
    main()