#include<iostream>
using namespace std;

class Book{
	public:
		string title;
		string author;
		int pages;
		Book(){
			title="no title";
			author="no author";
			pages=0;
		}
		Book(string aname,string aauthor,int apages){
			title=aname;
			author=aauthor;
			pages=apages;
			cout<<"Creating object"<<endl;
		}
};

int main(){
	
	string name="Mike";
	double pi = 3.14;
	char favoriteLetter ='G';
	
	Book book1("Harry Potter","JK Rowling",500);

	
	Book book2("Hr","J",700);
	book2.author="kjadsf";
	
	cout << book1.title<< " "<< book2.author;
	
	
	return 0;
}
