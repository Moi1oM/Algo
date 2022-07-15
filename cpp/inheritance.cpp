#include<iostream>
using namespace std;

class Chef{
	public:
		void makeChicken(){
			cout<<"The chef maeks chicken"<<endl;
		}
		void makeSalad(){
			cout<<"The chef maeks salad"<<endl;
		}
		void makeSpecialDsih(){
			cout<<"The chef makes bbq ribs"<<endl;
		}
};

class ItalianChef : public Chef{
	public:
		void makePasta(){
			cout<<"The chef makes pasta";
		}
		void makeSpecialDish(){
			cout<<"The chef makes chicken pasta"<<endl;
		}
};

int main(){
	Chef chef;
	chef.makeChicken();
	ItalianChef italianChef;
	italianChef.makeChicken();
	italianChef.makePasta();
	italianChef.makeSpecialDsih();
	return 0;
}
