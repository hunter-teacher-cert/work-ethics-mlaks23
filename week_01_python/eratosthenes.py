#n = int(input("Enter a whole number up to 100: "))

while True:
    try:
        n = int(input("Enter a whole number up to 100: "))
        break
    except ValueError:
        print("Please enter a number between 2 and 100")

def numbers_list(n):
    list = []
    for i in range (n - 1):
        list.append(i + 2)  #Starting with 2 since 2 is the first prime number
    return(list)

print()
print("Here is your list: ")
print(numbers_list(n))

print()
print("These are prime numbers up to " + str(n) + ": ")
def is_prime(): 
    print("2")
    print("3")
    print("5")
    print("7")
    for x in numbers_list(n):
        if (x % 2 == 0) or (x % 3 == 0) or (x % 5 == 0) or  (x % 7 == 0):
            print("-")
        else:
            print(x)
    
is_prime()



        

    


