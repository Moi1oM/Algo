#include<iostream>
#include<cmath>

using namespace std;

int main(){
	bool isMale=true;
	bool isTall=true;
	
	if(isMale && isTall){
		cout << "You are a tall Male";
	} else if(isMale && !isTall){
		cout << "You are short Male";
	} else if(!isMale && isTall){
		cout<< "You are tall but not male";
	} else{
		cout << "You are not Male and short";
	}
	return 0;
}
