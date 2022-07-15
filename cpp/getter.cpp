#include<iostream>
using namespace std;

class Movie{
	private:
		string rating;
	public:
		string title;
		string director;
		Movie(string aName,string aMajor,string arating){
			title =aName;
			director = aMajor;
			rating= arating;
		}
		void setRating(string aRating){
			rating = aRating;
		}
		string getRating(){
			return rating;
		}
};

int main(){
	Movie movie1("aver","aefa","Dog");
	movie1.setRating("hihi");
	cout<<movie1.getRating();
	return 0;
}
