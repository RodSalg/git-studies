def hello_world():
    print("hello world")

def sum(first_number: float, second_number: float) -> None:
    print(f"the sum of {first_number} + {second_number} is {first_number + second_number}")

def main():
    hello_world()
    sum(1, 5)

if __name__ == "__main__":
    main()