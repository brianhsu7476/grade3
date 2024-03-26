#include <bits/stdc++.h>
using namespace std;
#define kN 1003

int n, m, k=10;
char a[kN][kN];

signed main(){
	n=m=2*k+3;
	for(int i=0; i<n; ++i)for(int j=0; j<m; ++j){
		a[i][j]=' ';
		if(i==0||i==n-1||j==0||j==m-1)a[i][j]='%';
	}
	a[k+1][k+1]=a[1][k+1]=a[k+1][1]=a[k+1][2*k+1]='.';
	a[k+2][k+1]='P';
	a[k+2][k]=a[k+2][k+2]='%';
	for(int i=0; i<n; ++i){
		for(int j=0; j<m; ++j)cout<<a[i][j];
		cout<<endl;
	}
}
