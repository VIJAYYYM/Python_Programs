def check_weirdness(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")

# Read the input from a single line
n = int(input().strip())
check_weirdness(n)
