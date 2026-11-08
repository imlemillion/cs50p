#print("Hi there. This is your adding calculator:")

#x = float(input("what's x? "))
#y = float(input("what's y? "))

#z = round(x + y)

#print("The result is:", f"{z:,}")


#print("Hi there. This is your division calculator:")

#x = float(input("what's x? "))
#y = float(input("what's y? "))

#z = x + y

#print("The result is:", f"{z:.2f}")

def main():
    x = int(input("what's x? "))
    print("x cubed is", cubed(x))

def cubed(n):
    return pow(n,3)

main()