#include <stdio.h>
//exercise12
/*void main() {
	int i=1;
	for (i = 100; i <= 200; i += 2)
		printf("%d\n", i);

}

//exercise13

void main() {
	float i = 1;
	for (i = 0; i <= 5; i += 0.5)
		printf("%.1f\n", i);
}

//exercise14

void main() {
	int i, score, scores;
	float average;
	scores = 0;
	average = 0;
	for (i = 1; i <= 7; i += 1) {
		printf("Enter here your scores\n");
		scanf_s("%d", &score);
		scores += score;
		average = scores / 7;
	}
	printf("Your average score is: %.1f", average);

}*/

//exercise16

/*void main() {

	int i, factorial, input;
	factorial = 1;
	printf("Enter the number here: ");
	scanf_s("%d", &input);
	for (i = 1; factorial < input;i++) {
		factorial *= i;
	}
	if (factorial == input)
		printf("This is a factorial number.");
	else
		printf("This is not a factorial number");
	printf("%d", factorial);
}*/

//exercises17 high number
/*#include <limits.h>
void main() {
	int i, number, high = INT_MIN;

	for (i = 1; i <= 10; i++) {
		printf("Enter a number >>>\n");
		scanf_s("%d", &number);
		if (high < number)
			high = number;
	}
	printf("The bigest number is: %d", high);
}*/

//exercises18 common division

/*void main() {
	int i, number1, number2, consol_number1;

	printf("Enter here 2 numbers, When the first number should be the smallest one >>>");
	scanf_s("%d %d", &number1, &number2);
	consol_number1 = number1;

	for (; number1 > 0; number1 = number1 - 1) {
		if (number2 % number1 == 0 && consol_number1 % number1 == 0)
			printf("%d \n", number1);
	}
}*/

//exercises19 calculate exponent

/*void main() {
	int number1, number2, i, exponent;
	printf("Enter here 2 numbers >>> \n");
	scanf_s("%d %d", &number1, &number2);
	exponent = number1;

	for (i = 1; i < number2; i++) {
		number1 *= exponent;

	}
	printf("%d", number1);
}*/

//exercises20 sum of 10 numbers
/*void main() {

	int i, number, sum_of_number;
	sum_of_number = 0;

	for (i = 1; i <= 10; i++) {
		printf("Enter a number >>> \n");
		scanf_s("%d", &number);
		sum_of_number += number;

	}
	if (sum_of_number > 0)
		printf("The sum of the numbers is bigger than 0");
	else if (sum_of_number == 0)
		printf("The sum of numbers is exactly 0");
	else
		printf("the sum of numbers is less than 0");

}*/

//exercises21 

/*void main() {
	float i, number, sum_of_numbers,average;

	sum_of_numbers = 0;
	number = 1;


	for (i = 1;number != 0 ; i++) {
		printf("Enter here the number >>> ");
		scanf_s("%f", &number);
		sum_of_numbers += number;

	}
	i = i - 2;
	average = sum_of_numbers / i;
	printf("The sum of the numbers is: %.2f\n The number of times you entered a number is %.2f \n The average number is %.2f", sum_of_numbers, i, average);
}*/


//exercises 22
/*void main() {

	int number = 1, i = 0;

	while (number < 100) {
		printf("Enter a number >>> ");
		scanf_s("%d", &number);
		i++;
	}
	printf("The number of times you have dilayd numbers is: %d ", i);
}*/


//exercises23 divisible numbers

/*void main() {
	int number1 = 2, number2 = 3, i = 0;

	while (number1 % number2 != 0 && number2 % number1 != 0) {
		printf("enter 2 numbers with a space between them >>>");
		scanf_s("%d%d",&number1,&number2);
		i++;
	}
	printf("The number of times you have dilayd numbers is: %d and the right divisible numbers is: %d %d ", i, number1, number2);

}*/

//execises 24 palindrome


//4n --O(N)
void main() {
	int number, copy_number, exponent = 1;

	printf("Enter a number>>>");
	scanf_s("%d", &number);
	copy_number = number;


	while (number > 9) //n
	{
		exponent *= 10;
		number = number / 10;
	}

	for (; exponent != 0 && exponent != 1;) {
		if (copy_number % 10 == copy_number / exponent) {
			copy_number = copy_number / 10;
			exponent /= 10;
			copy_number = copy_number % exponent;
			exponent /= 10;
		}
		else {
			printf("not philindrome");
			break;
		}
	}
	if (exponent == 0 || exponent == 1)
		printf("philindrom");
}