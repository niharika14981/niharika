#importing modules
import addition
import subtration
import multiplication
import division
import modulusDivision

operations=(
    "1. addition \n",
    "2. subtration \n",
    "3. multiplication \n",
    "4. division \n",
    "5. modulusDivision",
)


if __name__=="__main__":
    print(*operations)
    choice=int(input("enter a choice btw 1-5"))
    if choice==1:
        n=int(input("enter 1st value"))
        m=int(input("enter 2nd value"))
        res= addition.add(n,m)
        print(f"sum of two numbers {res} ")
    elif choice==2:
        n=int(input("enter 1st value"))
        m=int(input("enter 2nd value"))
        res=subtraction.sub(n,m)
        print(res)
    elif choice==3:
        n=int(input("enter 1st value"))
        m=int(input("enter 2nd value"))
        res=multification.mul(n,m)
        print(res)
    elif choice==4:
        n=int(input("enter 1st value"))
        m=int(input("enter 2nd value"))
        res=division.div(n,m)
        print(res)
    elif choice==5:
        n=int(input("enter 1st value"))
        m=int(input("enter 2nd value"))
        res=modulusDivision.mod(n,m)
        print(res)
else:
    print("Please choice 1 to 5 operation")