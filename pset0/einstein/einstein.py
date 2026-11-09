def main():
    mass = int(input("enter mass in kg: "))
    print("Energy = ", energy(mass))

def energy(mass):
    c = 300000000
    return mass * pow(c,2)

main()
