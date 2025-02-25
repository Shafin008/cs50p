def main():
    mass = input('m: ')
    print(f"E: {energy(mass)}")

def energy(m):
    m = int(m)
    c = 300000000
    return m * c**2

main()
