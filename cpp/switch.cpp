#include<iostream>
using namespace std;

string getDayOfWeek(int dayNum){
	string dayName;
	switch(dayNum){
		case 0:
			dayName = "Sunday";
			break;
		case 1:
			dayName = "Monday";
			break;	
		case 2:
			dayName = "Tuesday";
			break;
		case 3:
			dayName = "Wedsnday";
			break;
		default:
			dayName ="Invalid day";
	}
	return dayName;
}

int main(){
	cout<<getDayOfWeek(2);
	return 0;
}
