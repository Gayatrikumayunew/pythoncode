num1=18


guesses=0
print("number of guesses is 8 only")
while(guesses<=8):
    num2=int(input("enter no"))

    if num2<18:
        print(" more towards greator number no")


    elif num2>18:
        print("try towards lesser number ")

    else :
        print(" right  number")

        break
    print("number of guesses left",8-guesses)
    guesses=guesses+1


if (guesses>8):
    print("game over45"
          "")


