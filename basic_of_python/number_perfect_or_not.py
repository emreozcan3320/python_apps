# Find a number ,that get as input, perfect or not

def main():
    num1 = int(input("Please enter the number to check it is perfect or not ? --> "))
    sum = 0
    for i in range(1,num1):
        if num1 % i == 0:
            sum += i
    if sum == num1:
        print("it is a perfect number")
    else: 
        print("it is not a perfect number")

    
if __name__ == "__main__":
    main()
