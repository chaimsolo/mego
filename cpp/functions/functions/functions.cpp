#include <stdio.h>




//exersices 31 factorial in function
	/*long getFactorial(int num) {
		int i;
		long result =1;

		for (i = 1; i <= num; i++) {
			result *= i;
        }
		return result;

    }

	void main() {
		long myResult;
		int number;

		printf("Enter the number >>> ");
	    scanf_s("%ld", &number);

		myResult = getFactorial(number);
		printf("The factorial of the number you have entered is: %ld", myResult);
	}*/
//exersices 32
/*long primaryNumber(int num) {
	int i;

	for (i = 2; i < num; i++) {
		if (num % i == 0) {
			printf("The number %d is not a primary number", num);
			return num;
		}
		printf("The number % d is  a primary number", num);
		return num;
		
	}
}
void main() {
	int number;

	printf("Enter a number >>> ");
	scanf_s("%d", &number);

	primaryNumber(number);

}*/

//exersices 33

/*long polindromNumber(int num) {
	int number1 = 0, number2 = num;
	for (num; num > 0; num % 10) {
		number1 = number1 * 10 + num % 10;
		num = num / 10;
	}
	if (number1 == number2)
		printf("the number %d is a polindrom number", number2);
	else
		printf("the number %d is not a polindrom number", number2);
	return num;
}
void main() {
	int number;
	printf("Enter a number >>> ");
	scanf_s("%d", &number);
	polindromNumber(number);
}*/


