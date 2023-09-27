#include <stdio.h>

void main()
{
	float a, b, c;
	printf("Enter here the first side of triangle:\n");
	scanf_s("%f", &a);
	printf("Enter here the second side of triangle:\n");
	scanf_s("%f", &b);
	printf("Enter here the third side of triangle:\n");
	scanf_s("%f", &c);
	if (a + b <= c || a + c <= b || b + c <= a)
		printf("Your triangle is an iilegal triangle!!!");
	else
		printf("Your traingle is a legal traingle!!!");

}