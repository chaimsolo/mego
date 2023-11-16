#include <stdio.h>
#include <math.h>




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
			printf("%d", i);
			return 1;
		}
		
		
	}
	printf("The number %d is  a primary number", num);
	printf("%d", i);
	return 0;
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
	for (num; num > 0;) {
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


//exersics 35 perfekt number

/*long isPerfect(long num) {
	
	long i, sumOfDividers = 0;

	for (i = 1; i < num; i++) {
		if (num % i == 0) {
			sumOfDividers += i;
			printf("%d  ", i);
		}
	}
	if (sumOfDividers == num) {
		printf("The number %ld is a perfect number.\n", num);
		return 1;
	}
	else
		printf("the numbr %d is not a perfect number.", num);
	return 0;
}

long main() {
	long number;

	printf("Enter here a number >>> ");
	scanf_s("%ld", &number);
	isPerfect(number);
}*/

/*long main() {
	long i, number, check;

	printf("Enter a number to chek if ther is a perfect numbers in the range >>> ");
	scanf_s("%ld", &number);
	for (i = 1; i <= number; i++) {
		isPerfect(i);
	}
}*/


//exersices 34 1089 number

/*int number1089(int num) {

	int i, oppositeNumber = 0, oppositeNumber1 = oppositeNumber, copyNumber = num, num1 = num, check, coppyCheck, oppositeI = 0;

	for (i = 1; i <= 3; i++) {
		oppositeNumber = oppositeNumber * 10 + copyNumber % 10;
		copyNumber /= 10;
	}
	if (num > oppositeNumber) {
		check = num - oppositeNumber;
	}
	else {
		check = oppositeNumber - num;
		num1 = oppositeNumber;
		oppositeNumber1 = num;
	}
	coppyCheck = check;
	for (i = 1; i <= 3; i++ ) {
		oppositeI = oppositeI * 10 + coppyCheck % 10;
		coppyCheck /= 10;
	}
	if (check + oppositeI == 1089) {
		printf("You enterd the number %d, and the opposite of this is %d,\nand %d - %d is %d, and %d + %d is 1089", num, oppositeNumber, num1, oppositeNumber1, check, check, oppositeI);
	}
	else
		printf("The number %d is a polindrom number", num);
	return 1;
}


int main() {

	int number;

	printf("Enter a number  with 3 digiets >>> ");
	scanf_s("%d", &number);
		
	number1089(number);
}*/



/*
//exersices 36 

#include <stdlib.h>
#include <time.h>
int countDividers(int num) {
	int i, numberOfDividers = 0;

	for (i = 1; i <= num / 2; i++) {
		if (num % i == 0) {
			numberOfDividers += 1;
		}

	}
	return numberOfDividers;
}

void checkingMaximumDividers(int max) {
	int i, maxNumberOfDividers = 0, numberOfDividers, randomNumber, maxRandomNumber = 0;
	


	for (i = 1; i <= 10; i++) {
		randomNumber = rand() % max + 1;
		numberOfDividers = countDividers(randomNumber);
		if (numberOfDividers > maxNumberOfDividers or i == 1) {
			maxNumberOfDividers = numberOfDividers;
			maxRandomNumber = randomNumber;
		}
		printf("   %d                   %d\n", randomNumber, numberOfDividers);
	}
	printf("The number with the maximum dividers is: %d, with %d dividres.", maxRandomNumber, maxNumberOfDividers);
}

void main() {
	int number;
	srand(time(NULL));
	printf("Enter the range of number that you want to check >>> ");
	scanf_s("%d", &number);
	printf("\nnumber          number of dividers\n");
	
	checkingMaximumDividers(number);


}*/