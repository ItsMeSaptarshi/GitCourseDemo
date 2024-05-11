import math

def trig_calculator():
    print("Enter the angle in degrees: ")
    angle = float(input())

    print("Choose an operation (+, -, *, /): ")
    operation = input().strip()

    if operation == "+":
        print("Enter the first trigonometric function: ")
        func1 = input().strip()
        print("Enter the second trigonometric function: ")
        func2 = input().strip()
        result = eval(f"math.{func1}(math.radians({angle})) + math.{func2}(math.radians({angle}))")
    elif operation == "-":
        print("Enter the first trigonometric function: ")
        func1 = input().strip()
        print("Enter the second trigonometric function: ")
        func2 = input().strip()
        result = eval(f"math.{func1}(math.radians({angle})) - math.{func2}(math.radians({angle}))")
    elif operation == "*":
        print("Enter the first trigonometric function: ")
        func1 = input().strip()
        print("Enter the second trigonometric function: ")
        func2 = input().strip()
        result = eval(f"math.{func1}(math.radians({angle})) * math.{func2}(math.radians({angle}))")
    elif operation == "/":
        print("Enter the first trigonometric function: ")
        func1 = input().strip()
        print("Enter the second trigonometric function: ")
        func2 = input().strip()
        result = eval(f"math.{func1}(math.radians({angle})) / math.{func2}(math.radians({angle}))")
    else:
        print("Invalid operation!")
        return

    print(f"The result is: {result}")


if __name__ == "__main__":
    trig_calculator()