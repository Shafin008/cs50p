def main():
    inp = input()
    print(convert(inp))

def convert(user):
    return user.strip().replace(':)', '🙂').replace(':(', '🙁')

main()
