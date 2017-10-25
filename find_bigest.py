#Find the biggest number from 3 that given by user
def main():
    arr = []
    num1 = int(input("Please enter first number --> "))
    arr.append(num1)
    num2 = int(input("please enter second number --> "))
    arr.append(num2)
    num3 = int(input("please enter third number --> "))
    arr.append(num3)
    sorted_arr = sorted(arr)
    len_of_sorted_arr= len(sorted_arr)
    print("the bigest number is ",sorted_arr[len_of_sorted_arr-1])    
    

if __name__ == "__main__":
    main()
