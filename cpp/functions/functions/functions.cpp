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

//exersices 37 goldbach

/*int isPrime(int num) {
	int i, result = (int)sqrt(num);

	for (i = 2; i <= result; i++) {
		if (num % i == 0) {
			return 0;
		}
    
	}
	return 1;


}

void twoPrimes(int num) {
	int i, j, w, flag;
	int prime1, prime2;
	for (w = 6; w <= num; w += 2) {
		flag = 1;
        for (i = 2; i <= num; i++) {
			if (flag == 0) {
				break;
			}
	    	if (isPrime(i) == 1){
		    	prime1 = i;
			    for (j = i; j <= num; j++) {
				    if (isPrime(j) == 1) {
					    prime2 = j;
						if (prime1 + prime2 == w) {
							printf("%d + %d = %d\n", prime1, prime2, w);
							flag = 0;
							break;
						}


				}
			}
			}
		}

	}
}

void main() {
	int number;
	printf("Enter a number >>> ");
	scanf_s("%d", &number);
	twoPrimes(number);
}*/


/*
#include <stdlib.h>
#include <time.h>
#define SIZE  9

void displayElementsInArrWithLength(int arr[], int lenghth) {
	int i;

	for (i = 0; i < lenghth; i++) {
		printf("%d: %d \n", i + 1, arr[i]);
	}
}

void displayElementsInArr(int arr[]) {
	int i;
	
	for (i = 0; arr[i] != -1 ; i++) {
		printf("%d: %d\n", i + 1, arr[i]);
	}
    
}

void main() {
	srand(time(NULL));
	int arr1[SIZE], i;
	int arr2[] = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, -1 };

	for (i = 0; i <= 9; i++) {
		arr1[i] = rand() % 101;

	}
	displayElementsInArrWithLength(arr1, SIZE);
	printf("\n\n\n\n");

	displayElementsInArr(arr2);
	printf("%d", arr2);
}
*/
//exersices 41 grades

#include <stdlib.h>
#include<time.h>

//define const varible
#define SIZE 13


void displayGrades(int grades[], int length) {

	int i;
	for (i = 0; i < length; i++) {
		//display grade with i loation
		printf("%d  ", grades[i]);
	}
	printf("\n\n");


}

//function that calcullate the grades for avarage and changing them

void averageGrades(int grades[], int length) {


	//declear vars
	int i, sum = 0;
	float average;
	const int EXTRA_GRADE = 7;
    
	for (i = 0; i < length; i++) {
		sum += grades[i];
	}
	average = sum / length;
	
	//checking if the averaga is less than 55

	if (average < 55) {
		for (i = 0; i < length; i++) {
			//adding the extra number
			grades[i] += EXTRA_GRADE;
			//limiting the ceiling to 100
			if (grades[i] > 100) {
				grades[i] = 100;
			}
		}
	}
}

// getting the grades by random
void main() {
	//using the clock for random
	srand(time(NULL));

	//declere var arr 
	int grades[SIZE];
	//declear var i
	int i;

	for (i = 0; i < SIZE; i++) {
		grades[i] = rand() % 101;
	}
	displayGrades(grades, SIZE);
    
	averageGrades(grades, SIZE);

	displayGrades(grades, SIZE);

}