#include <iostream>

using namespace std;

int main(){
	string phrase="Giraffe Academy";
	string phrasesub;
	phrasesub = phrase.substr(8,3);
	cout<< "Hi " ;
	cout<< "My name is " <<endl;
	cout<< phrase << endl;
	cout<< phrase.length();
	cout<< phrase[0];
	cout<< phrase.find("Academy", 0)<<endl;
	cout<< phrase.substr(8,3); //8번째 부터 3개
	cout<< phrasesub;
	
	return 0;
}
