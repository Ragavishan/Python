try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a another number:"))
    result=a/b
    print(f"result:{result}")
except ZeroDevisionError:
    Print("Error:Devision by zero is not allowed")
except ValueError:
    print("Error:Invalid input,please enter a number")
     