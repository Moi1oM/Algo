#include<bits/stdc++.h>
using namespace std;
int d[50][50];	
int n,m,posx,posy,dir;
bool clean[50][50];
bool isWallOrClean(int x,int y){
	if(clean[x][y]==true){
		return true;
	}
	if(d[x][y]==1){
		return true;
	}
	return false;
}
int main(){
	int px,py,ppx,ppy,loop=0;
	int dx[4]={-1,0,1,0};
	int dy[4]={0,-1,0,1};
	cin>>n>>m;
	cin>>posy>>posx>>dir;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			scanf("%d",&d[i][j]);
			clean[i][j]=false;
		}
	}
	bool check;
	while(true){
		check=false;
//		if(clean[posy][posx]==false)cout<<posx<<" "<<posy<<" "<<dir<<endl;
		clean[posy][posx]=true;
		px=posx+dx[dir];
		py=posy+dy[dir];
		for(int i=0;i<4;i++){
			ppx=posx+dx[i];
			ppy=posy+dy[i];
			if(isWallOrClean(ppy,ppx)==false)break;	
			if(i==3)check=true;
		}
		if(check){
			switch(dir){
				case 0:
					posy++;
					break;
				case 1:
					posx--;
					break;
				case 2:
					posy--;
					break;
				case 3:
					posx++;
					break;
			}
			if(d[posy][posx]==1)break;
		}else if(!isWallOrClean(py,px)){
			posx=px;
			posy=py;
			if(dir==0)dir=3;
			else dir--;		
		}else {
			if(dir==0)dir=3;
			else dir--;			
		}
	}
	int count=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(clean[i][j])count++;
			
		}

	}
	cout<<count;
	return 0;
}
