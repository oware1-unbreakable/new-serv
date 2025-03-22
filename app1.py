import sys
def sub(num1,num2):
        num3=num1-num2
        print(num3)
num1=int(sys.argv[1])
operator=sys.argv[2]
num2=int(sys.argv[3])
if operator == "sub":
    sub(num1,num2)
else :
      print("error")

