//PROGETTO
#include <iostream>
#include <stdio.h>
#include <stdbool.h>
#include <conio.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <string.h>
#include <stdlib.h>

// Funzioni necessarie:

float fattoriale(float n);
float fattoriale(float n)
{
	float fatt=1;
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


float CoBin( float n, float k);
float CoBin( float n, float k)
{
	float cobin;
	
	cobin= (fattoriale(n))/((fattoriale(n-k))*(fattoriale(k)));
	
	return cobin;
}

float pot( float b, float e);
float pot( float b, float e)
{
	float p=1;
	for(float i=1;i<=e;)
	{
		p=b*p;
		i++;
	}
	return p;
}






// Termine funzioni necessarie

//Funzioni chiave

float alfa(float vb, float k);
float alfa(float vb, float k)
{
	float a; // coefficiente soluzione
	float sigma=0;
	
	float n= vb-1;
	float i=0 ;
	
	for(;n>=i;)
	{
		sigma= sigma+alfa(i,k)*CoBin(2*vb-2*i,vb-i);
		i++;
	}
	
	a= CoBin(2*vb+k,vb+k)-sigma;
	
	
	return a;
}

float FailEtVb (float vb, float k, float p, float b);
float FailEtVb(float vb, float k, float p, float b)
{
	float prob;
	prob= alfa(vb,k)*pot(p,vb+k)*pot(b,vb);
	
	return prob;
}




// Termine funzioni chiave


main()
{
system ("COLOR F0");
system ("TITLE Il pollo e il banco");

float k=1; // soldi iniziali
float vb=0, vp=0; // # vittorie del (vb) banco e del (vp) pollo.
float p=0.499, b=0.501;  // probabilità di vincere del (p) del pollo e (b) del banco.
float fail; // probabilità di fallimento

for(;k<200;)
{
	printf("\n\n\nSoldi iniziali: %.0f\n\n",k);
		for(;fail<0.500;)
		{
		fail=fail+FailEtVb(vb,k,p,b); 
		printf("\nVitt.Banco:%.0f		Prob.fail:%f",vb,fail);
		printf(" Disposizioni legali: %.0f ",alfa(vb,k));
	
		vb++;
		}
	fail=0;
	vb=0;
	k++;
}
getchar();
return 0;
}




