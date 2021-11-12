#include <iostream>

using namespace std;

int main(){
	// input
	int n,m;
	cin >> n >> m;
	int arr[n];
	int maxLeft = 0;
	for(int i=0; i<n; i++){
		cin >> arr[i];
		maxLeft = max(maxLeft,arr[i]);
	}

	// cal
	long left = maxLeft;
	long right = INT32_MAX;
	long middle;
	long result;
	while(left < right){
		long sum = 0;
		int cnt = 1;
		middle = (left+right)/2;
		for(int i : arr){
			sum+=i;
			if(sum > middle){
				sum=i;
				cnt++;
			}
		}
		if(cnt > m){
			left = middle+1;
		} else{
			right = middle-1;
			result = middle;
		}
	}

	// result
	cout << result;
	return 0;
}
