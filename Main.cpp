#include <iostream>
#include <stack>

using namespace std;

stack<int> s;

int main(void){
	int n;
	cin >> n;
	for(int i=0; i<n; i++){
		int num;
		cin >> num;
		if(num != 0) s.push(num);
		else s.pop();
	}
	int size = s.size();
	int result = 0;
	for(int i=0; i<size; i++){
		int temp = s.top();
		s.pop();
		result += temp;
	}
	cout << result;
	return 0;
}
