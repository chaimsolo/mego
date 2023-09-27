//exercises1 rectrangler area
/*#include <stdio.h>

void main() {
	int side1, side2, perimeter = 4, area = 4;
	printf("Enter the lenght of two sides of the rectangler:\n");
	scanf_s("%d %d", &side1, &side2);
	perimeter = (side1 + side2) * 2;
	area = side1 * side2;
	printf("The area of the rectangler is: %d \n The perimeter of the rectangler is: %d", area, perimeter);

}*/

//exercises2 discount

/*#include <stdio.h>

void main() {
	//declare vars
	int price, amount, discount;
	float total_price;
	//reciving input
	printf("Enter here the price, then enter the amount,\n then Enter the precentage of discount");
	scanf_s("%d %d %d", &price, &amount, &discount);
	//calculate
	//if we want to convert an integer number to  float, we need to put a point
	//after the integer  number in the calculation as the example below
	//(exept a case if integer is in a var).
	total_price = (price * amount) * (1.0 - discount / 100.0); 
	printf("The total price you need to pay is: %.2f", total_price);

}*/

//exercises3 averageof 3 greads
/*#include <stdio.h>

void main() {

	//declare vars
	int grade1, grade2, grade3;
	double average;
	//recieving input
	printf("Enter here your first test acore: \n");
	scanf_s("%d", &grade1);
	printf("Enter here your second test acore: \n");
	scanf_s("%d", &grade2);
	printf("Enter here your third test acore: \n");
	scanf_s("%d", &grade3);
	//calculation
	average = (grade1 + grade2 + grade3) / 3.0;
	//print calculation
	printf("your average score is:  %.f", average);
}*/

//exercises4 circle

/*#include <stdio.h>

void main() {
	//declare vars

	float radius, perimeter, erea, PI = 3.14;
	printf("Enter the radius of the chrcle >>> \n");
	scanf_s("%f", &radius);
	//calculate erea
	erea = PI * radius * radius;
	//calculate perimeter
	perimeter = 2 * radius * PI;
	//print results
	printf("The erae of the circle is: %.2f\n The perimeter of the circle is %.2f", erea, perimeter);

}*/

//exercises5 time

/*#include <stdio.h>

void main() {
	//declar vars
	int minutes, hours, total_time, total_minutes;
	//recive input
	printf("Enter te dsired time >>> \n");
	scanf_s("%d", &total_time);
	//calculate
	minutes = total_time % 100;
	hours = (total_time - minutes) / 100 * 60;
	total_minutes = minutes + hours;
	printf("The total minutes that have left since midnight is %d", total_minutes);
}*/

//exercises6 scores
/*#include <stdio.h>

void main() {
	//declare vars
	float score1, score2, score3, average;
	printf("Enter the tree scores >>> \n");
	scanf_s("%f %f %f", &score1, &score2, &score3);
	average = (score1 + score2 + score3) / 3;
	if (average < 55)
		printf("Your average is %.2f you need to improve your scores", average);
	else if (average < 90)
		printf("Your average is %.2f you are good, keep goinng in this way.", average);
	else
		printf("Your average is %.2f you are exelent!", average);
	
}*/
//exercises7 expenses
/*#include <stdio.h>

void main() {
	int monthly_expenses, yearly_exspenses;
	printf("Enter here your monthly expenses >>>");
	scanf_s("%d", &monthly_expenses);
	yearly_exspenses = monthly_expenses * 12;
	if (yearly_exspenses >= 100000)
		printf("Your yearly expenses is %d and it's bigger than 100000", yearly_exspenses);
	else
		printf("Your yearly expenses is %d and it's smaller than 100000", yearly_exspenses);
}*/

//exercises8 tools
/*#include<stdio.h>

void main() {
	float amount, price, sum_with_vat;
	
	printf("enter here the amount of units you want to buy >>> ");
	scanf_s("%f", &amount);
	printf("Enter here the expected price you have to pay >>> ");
	scanf_s("%f", &price);
	
	//calcullation
	sum_with_vat = amount * price * 1.17;
	if (sum_with_vat >= 10000)
		printf("The expected expenditure after VAT is above 10000 and it's actually %.2f", sum_with_vat);
	else
		printf("The expected expenditure after VAT is below 10000 and it's actully %.2f\n\n\n\n\n\n\n", sum_with_vat);
}*/



//exercises9 