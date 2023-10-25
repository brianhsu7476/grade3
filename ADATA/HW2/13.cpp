#include <bits/stdc++.h>
#define lld long long
#define endl '\n'
using namespace std;
#define oo 1000000000000000018
#define kN 5003

lld dp[kN];
int n, x[kN], y[kN];

lld d(int i, int j){
	lld dx=x[i]-x[j], dy=y[i]-y[j];
	return dx*dx+dy*dy;
}

void solve(){
	cin>>n;
	x[n+1]=y[n+1]=0;
	for(int i=1; i<=n; ++i)cin>>x[i]>>y[i], dp[i]=oo;
	dp[0]=0;
	for(int i=1; i<n+2; ++i){
		if(i==1)dp[0]=d(0, 1);
		else for(int j=0; j<i; ++j)dp[i-1]=min(dp[i-1], dp[j]+d(j, i));
		for(int j=0; j<i-1; ++j)dp[j]+=d(i-1, i);
		//for(int j=0; j<i; ++j)cout<<dp[j]<<" \n"[j==i-1];
	}
	lld ans=oo;
	for(int i=0; i<=n; ++i)ans=min(ans, dp[i]+d(i, 0));
	cout<<ans<<endl;
}

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	int T; cin>>T;
	while(T--)solve();
}
