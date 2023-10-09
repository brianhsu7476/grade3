#include <bits/stdc++.h>
#define int long long
#define endl '\n'
using namespace std;
#define oo 1000000000000000018
#define kN 1000006
int n, k, a[kN], sl[kN], sr[kN];

int solve(int l, int r){
	if(r-l<2)return a[l]>=k?1ll:oo;
	int m=l+r>>1, ans=min(solve(l, m), solve(m, r));
	sl[0]=sr[0]=0;
	for(int i=0, j=m-1; j>=l; ++i, --j)sl[i+1]=sl[i]+a[j];
	for(int i=0, j=m; j<r; ++i, ++j)sr[i+1]=sr[i]+a[j];
	for(int i=1; i<=m-l; ++i)sl[i]=max(sl[i], sl[i-1]);
	for(int i=1; i<=r-m; ++i)sr[i]=max(sr[i], sr[i-1]);
	for(int i=0, j=r-m; i<=m-l&&j>=0; ){
		if(sl[i]+sr[j]>=k)ans=min(ans, i+j), --j;
		else ++i;
	}
	return ans;
}

signed main(){
	ios::sync_with_stdio(0), cin.tie(0);
	int T; cin>>T;
	while(T--){
		cin>>n>>k;
		for(int i=0; i<n; ++i)cin>>a[i];
		int ans=solve(0, n);
		cout<<(ans==oo?-1:ans)<<endl;
	}
}
