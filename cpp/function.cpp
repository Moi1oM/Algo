#include<iostream>
#include<cmath>

using namespace std;

void sayHi(string name, int age){
	cout<<"Hello "<<name<<" You are "<<age<<endl;
}


int main(){
	int num;
	
	cout<<"top"<<endl;
	sayHi("Mike",12);
	sayHi("SW",30);
	sayHi("D",114);
	cout<<"bottom";
	return 0;
}
