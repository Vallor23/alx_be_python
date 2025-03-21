def check(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
def main():
    number = int(input("Enter a number: "))
    print(f"The number {number} is {check(number)}")

if __name__ == "__main__":
    main()