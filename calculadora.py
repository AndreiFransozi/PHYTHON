while True:
    print("1. Addition")
    print("2. Subtracion")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice"))
    if (choice>=1 and choice<=4):
        print("Enter two numbers: ")
        num1 = int(intput())
        num2 = int(intput())
        if choice == 1:
            res = num1 + num2
            print("Result =", res)
        if choice == 2:
            res = num1 - num2
            print("Result =", res)
        if choice == 3:
            res = num1 * num2
            print("Result =", res)
        else:
            res = num1 / num2
            print("Result =", res) elif choice == 5:
                exit()
            else:
                print("Wrong Input..!!")
