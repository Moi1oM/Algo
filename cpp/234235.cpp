#include <string>
#include <vector>
#include <iostream>

using namespace std;
int index=0,sizez;//sizez==2

void nextFood(){
    if(index==sizez)index=0;
    else index++;
}
int outFood(){
    if(index==0)return sizez;
    else {
    	index--;
    	return index;
	}
}

int solution(vector<int> food_times, long long k) {
    int answer,times=0;
    sizez=food_times.size()-1;
    while(true){
    	cout<<"index: "<<index<<" times: "<<times<<endl;
        if(food_times[index]==0)nextFood();
        else if(food_times[index]>0){
            food_times[index]--;
            times++;
            nextFood();
        }
        if(times==(k+1))break;
    }
    answer=outFood();
    return answer;
}
int main(){
	vector<int> v;
	v.push_back(3);
	v.push_back(1);
	v.push_back(2);
	long long k =5;
	cout<<solution(v,k);
	return 0;
}
