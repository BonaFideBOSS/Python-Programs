def program():
    num = int(input("Enter a prime number: "))

    arr = []
        
    if num > 1:
        for i in range(2, num):
            if (num % i ) == 0:
                print(num,"is not a prime number.")
                break
            
            check = True
            for j in range(2,i):
                if (i % j) == 0:
                    check = False
            if check == True:
                arr.append(i)
        else:
            arr.append(num)
            combine(arr,num)
    else:
        print("1 is not a prime number.")

    again()     


def combine(arr,userInput):
    if len(arr) > 1:
        print("\n===== List of prime numbers till " +str(userInput)+ " ====")
        total = 0
        for index, num in enumerate(arr):
            total = index + 1
            print(str(total) + ". ",num)

        print("\n===== All possible combinations =====")
        
        for i in arr:
            print("\n-----",i,"-----")
            combinations = list(findCombinations(arr,i))
            if len(combinations) > 0:
                for x,j in enumerate(combinations):
                    print("["+str(x+1)+"] "+' + '.join(str(item) for item in j)+" = "+str(i))
            else:
                print("No possible combination for",i)
    else:
        print("No possible combination for",userInput)


def findCombinations(numbers, target, partial=[]):
    if sum(partial) == target:
        if len(partial) > 1:
            yield partial
            
    if sum(partial) >= target:
        return
    
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from findCombinations(remaining, target, partial + [n])


def again():
    check_again = input('\nDo you want to run the program again? [Y/N]')

    if check_again.upper() == 'Y':
        program()
    elif check_again.upper() == 'N':
        print('See you later.')
    else:
        again()

program()
