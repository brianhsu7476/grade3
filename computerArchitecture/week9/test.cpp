#include <bits/stdc++.h>
using namespace std;
#define kN 1003

int x5[kN], x6[kN], nxt[kN], x29=10;

void output(int t, const string s){
	cout<<t<<' '<<x5[t]<<' '<<x6[t]<<' '<<s<<endl;
}

void upd(int *a, int id, int v){
	for(int i=id; i<kN; ++i)a[i]=v;
}

signed main(){
	int t=0;
	while(1){
		if(nxt[t])break;
		upd(nxt, t+4, x5[t]>=x29);
		output(t++, "blt");
		upd(x6, t+3, x5[t]+x6[t]);
		output(t++, "add");
		upd(x6, t+3, x6[t]+5);
		output(t++, "addi");
		upd(x5, t+3, x5[t]+1);
		output(t++, "addi");
	}
	for(int i=0; i<4; ++i)output(t+i, "");
}
