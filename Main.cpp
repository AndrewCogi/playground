#include <iostream>

using namespace std;

int func(int num){
	int result = 1;
	for(int i=num; i>0; i--){
		result*=i;
	}
	return result;
}

int main(void){
	int n;
	cin >> n;
	cout << func(n);
	return 0;
}
