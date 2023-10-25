#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
#define kN 500005
#define oo 1000000007

struct P{
	int c, s, i;
	P(){}
	P(int c, int s):c(c), s(s){}
	bool operator<(const P r)const{return c>r.c||c==r.c&&s<r.s;}
};

int n, bit[kN], id[kN], ans[kN], ans2[kN];
P a[kN];

void upd(int x, int v){
	for(int i=x+1; i<=n; i+=i&-i)bit[i]=min(bit[i], v);
}

int qry(int x){
	int ret=oo;
	for(int i=x; i; i-=i&-i)ret=min(ret, bit[i]);
	return ret;
}

void solve(){
	int g, sz;
	cin>>n>>g, --g;
	for(int i=0; i<n; ++i)cin>>a[i].c, a[i].i=id[i]=i, bit[i+1]=oo;
	for(int i=0; i<n; ++i)cin>>a[i].s;
	sz=a[g].s;
	sort(a, a+n);
	sort(id, id+n, [](int i, int j){return a[i].s<a[j].s;});
	for(int i=0; i<n; ++i){
		if(!a[id[i]].s){upd(id[i], ans[id[i]]=0); continue;}
		int j=lower_bound(a, a+n, P(a[id[i]].s, oo))-a;
		upd(id[i], ans[id[i]]=min(qry(j)+1, oo));
	}
	for(int i=0; i<n; ++i){
		if(a[i].i==g)ans2[a[i].i]=0;
		else if(a[i].c<sz||ans[i]>=oo)ans2[a[i].i]=-1;
		else ans2[a[i].i]=ans[i]+1;
	}
	for(int i=0; i<n; ++i)cout<<ans2[i]<<" \n"[i==n-1];
}

int main(){
	int T; cin>>T;
	while(T--)solve();
}
