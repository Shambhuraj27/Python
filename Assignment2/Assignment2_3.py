
def main():
    print("Enter the number :")
    No = int(input())
    a = 1
    for i in range(No,1,-1):
        a = a * i
    print("The factorial is ",a)

if __name__ == "__main__":
    main()



