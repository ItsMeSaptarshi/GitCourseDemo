import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            double num1, num2;
            char operation;

            System.out.println("Enter the first number: ");
            num1 = scanner.nextDouble();

            System.out.println("Enter the second number: ");
            num2 = scanner.nextDouble();

            System.out.println("Enter the operation (+, -, *, /): ");
            operation = scanner.next().charAt(0);

            switch (operation) {
                case '+':
                    System.out.println("The result is: " + (num1 + num2));
                    break;
                case '-':
                    System.out.println("The result is: " + (num1 - num2));
                    break;
                case '*':
                    System.out.println("The result is: " + (num1 * num2));
                    break;
                case '/':
                    if (num2 != 0) {
                        System.out.println("The result is: " + (num1 / num2));
                    } else {
                        System.out.println("Error! Division by zero is not allowed.");
                    }
                    break;
                default:
                    System.out.println("Invalid operation!");
            }
        }
    }
}