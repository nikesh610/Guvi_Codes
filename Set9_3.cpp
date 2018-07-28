#include <iostream>
using namespace std;

int main() {
	char c;
	int f1,f2;
	cin>>f1>>c>>f2;
	if(c=='/')
	{
		cout<<f1/f2;
	}
	else{
		cout<<f1%f2;
	}
}
