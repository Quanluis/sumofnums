def main():
    
    print("Sum of odd and even numbers")
    print("===========================")
    answer = int(input("Enter a whole number between 1 and 50: "))

    while True:
        if answer <= 50 and answer > 0:
            break
        else:
            answer = int(input("Try again, Your number must be between 1 and 50: "))
            continue

    if (answer % 2) == 0:
        print(answer, "is even")
        num = range(0,answer + 2,2)
    else:
        print(answer, "is odd")
        num = range(1,answer + 2,2)
            
    for n in num:
        x = sum(num)

    if (answer % 2) == 0:
        print("Sum of  all numbers between 2 and ", n , " is ", x)
    else:
        print("Sum of  all numbers between 1 and ", n , " is ", x)


    tryAgain = input("Try again? Y/N")

    if(tryAgain == "y" or tryAgain == "Y"):
        print("You pressed yes")
        main()
    elif(tryAgain == "n" or tryAgain == "N"):
        exit()    
main()

    







