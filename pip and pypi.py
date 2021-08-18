print("i will always run")
print(f'{__name__}')



def main():
    print("im a main function is firstpgm")

def sub():
    print("i will run only during import")


if __name__ == "__main__":
    main()
else:
    sub()

