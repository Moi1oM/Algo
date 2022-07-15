#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int secretNum=7;
	int guess,guessCount=0;
	int guessLimit=3;
	bool outOfGuess=false;
	
	while(secretNum!=guess && !outOfGuess){
		if(guessCount <guessLimit){
			cout << "Enter guess: ";
			cin >> guess;
			guessCount++;
		} else{
			outOfGuess=true;
		}
 		
	}
	if(outOfGuess){
		cout<< "You Lose" << endl;
	} else{
		cout<< "You Win!"<<endl;
	}
	
	return 0;
}
