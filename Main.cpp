#include <iostream>
#include <algorithm>

using namespace std;

int main(void){
	int n;
	cin >> n;
	int arr1[n];
	int arr2[n];
	for(int i=0; i<n; i++){
		cin >> arr1[i];
	}
	for(int i=0; i<n; i++){
		cin >> arr2[i];
	}
	// sorting
	sort(arr1,arr1+n);
	sort(arr2,arr2+n);
	// cal
	int result = 0;
	for(int i=0; i<n; i++){
		result += arr1[i]*arr2[n-i-1];
	}
	cout << result;
	return 0;
}
