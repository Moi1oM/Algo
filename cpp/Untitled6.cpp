#include<iostream>
#include<cmath>

using namespace std;

int main(){
	int age=30;
	string name;
//	cout << "Enter your age: ";
//	cin >> age;
	cout<< "Enter your name : ";
	getline(cin, name);
	cout << "You are "<< age << " years old"<<endl;
	cout << "Hello " << name<< "!"<<endl;
	return 0;
}
