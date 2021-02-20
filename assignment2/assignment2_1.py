import arithmatic

def main():
    print("enter the number")
    value1=int(input())
    print("enter the number")
    value2=int(input())
    
    a=arithmatic.add(value1,value2)
    b=arithmatic.mult(value1,value2)
    c=arithmatic.div(value1,value2)
    d=arithmatic.sub(value1,value2)
    
    print("addition is :",a)
    print("multiplication  is :",b)
    print("division is :",c)
    print("subtraction is :",d)
    


if __name__=="__main__":
    main()
    