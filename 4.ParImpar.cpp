//Edwin Aaron Garcia Pulido
//Programa que identifica si un número es par o impar

#include <iostream>
#include <cstdlib>
using namespace std;

int main() 
{
	int num=0;
	cout<<"Ingrese el numero: ";
	cin>>num;
	if (num%2==0)
	{
		cout<<"El n\243mero "<<num<<" es par"<<endl;
	}
	else
	{
		cout<<"El n\243mero "<<num<<" es impar"<<endl;
	}
	return 0;
}
