def hello_world():
    print("hello world")

def sum(first_number: float, second_number: float) -> None:
    print(f"the sum of {first_number} + {second_number} is {first_number + second_number}")

def multiplication_two_numbers(first_number: float, second_number: float) -> None:
    print(f"the product of {first_number} times {second_number} is {first_number * second_number}")

def main():
    hello_world()
    sum(1, 5)
    multiplication_two_numbers(2, 10)

if __name__ == "__main__":
    main()