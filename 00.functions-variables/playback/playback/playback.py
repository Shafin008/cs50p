def main():
    inp = input()
    print(speed(inp))

def speed(user):
    return user.strip().replace(" ", "...")


main()
