/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

void to_binary(int n, int * array, int index){
    if (n / 2 != 0)
        to_binary(n / 2, array, index + 1);
	array[index] = n % 2;
}

int main(){
	long long unsigned int product = 1;
	int tens = 0;
	int twos = 0;

	for(int i = 1; i <= 100; i++){
		if(i % 10 == 0){
			product *= i / 10;
			tens += log10(i);}
		else if(i % 2 == 0)
			twos += log2(i);
		else
			product *= i;
	}

	int length = 26;
	int * bits = new int [length];
	to_binary(product, bits, 0);
	for(int i = length - 1; i >= 0; i--)
		cout << bits[i];
	cout << "" << endl;
	cout << "twos: " << twos << endl;
	cout << "tens: " << tens << endl;
	cout << "product: " << product << endl;

return 0;}
