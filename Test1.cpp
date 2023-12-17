//PROGETTO
#include <iostream>
#include <stdio.h>
#include <stdbool.h>
#include <conio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <string.h>
#include <stdlib.h>

int fattoriale(int n);
int fattoriale(int n)
{
	int fatt=1;
if(n==0)
{
	return 1;
}
	for(;n>1;)
	{
		fatt= fatt*n;
	
		n=n-1;
	}
	
	return fatt;
}

float pot( float b, float e);
float pot( float b, float e)
{
	float p=1;
	for(int i=1;i<=e;)
	{
		p=b*p;
		i++;
	}
	return p;
}

int CoBin( int n, int k);
int CoBin( int n, int k)
{
	int cobin;
	
	cobin= (fattoriale(n))/((fattoriale(n-k))*(fattoriale(k)));
	
	return cobin;
}

int sigma(int n, int i);
int sigma(int n, int i)
{
	int sigma;
	for(;n>i;)
	{
		
		i++;
	}
	return sigma;
	
	
}


main()
{

system ("TITLE Test  funzione fattoriale");
int n=0;
int d= fattoriale(n);
	printf("%d",d);
	printf("\n\n\n%d",CoBin(3,2));
	
	printf("\n\n%f",pot(2,3));
	
return 0;
}



