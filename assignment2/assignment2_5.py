def gun(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return True
                break
    else:
        return False


def main():
    print("enter the number")
    value=int(input())
    ret=gun(value)
    if ret == True:
        print(value ,"is not prime number")
    else:
        print(value," is prime number")


if __name__=="__main__":
    main()