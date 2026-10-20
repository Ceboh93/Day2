firstNumber= int(input("Enter First number :"))
secondNumber= int(input("Enter second number:"))

if firstNumber < secondNumber:
    hcf = firstNumber
else:
        hcf = secondNumber
        
while firstNumber % hcf !=0 or secondNumber % hcf !=0:
        hcf = hcf - 1
        
print("The highest common factor is:", hcf)