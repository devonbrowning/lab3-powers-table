# Define tables
def multiplication_table(n):
# end means it will wait and print at the end
# \n means new line?
# TITLE
    print("\nMultiplication Table:")

# COLUMN HEADERS
    print("    ", end="")  # 'end=""' -- making sure nothing is printed after the spaces in the print statement
    for i in range(1, n + 1):
        print(f"{i:4}", end="")  # i:4 specifies 4 digits total

# COLUMN CUTOFF
    print("\n    =", end="")
    for i in range(1, n + 1):
        print("====", end="")
    print()

# ROW HEADER
    for i in range(1, n + 1):
        print(f"{i:2} |", end="")

# INSIDE TABLE
        for column in range(1, n + 1):
            print(f"{i * column:4}", end="")
        print()

def insert_table(n):
    print("Number   Squared     Cubed")
    print("======   =======     =====")
    for i in range(1, n + 1):
        print(f" {i}\t\t\t{i ** 2}\t\t\t{i ** 3}")

    multiplication_table(n)

print("How well do you know your squares and cubes?")

while True:
    num = int(input("Please enter an integer: "))
    insert_table(num)
    choice = input("Would you like to continue? (y/n)")
    if choice != "y":
        break