#include <bits/stdc++.h>
#define int long long
#define endl '\n'
using namespace std;
#define kN 1503
#define kM 500005
int n, m, a[kN][kN], k, sa[kN][kN], dp[kN], dp0[kN];

signed main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n>>m;
	for(int i=0; i<n; ++i)for(int j=0; j<m; ++j)cin>>a[n-1-i][m-1-j];
	for(int i=0; i<n; ++i)for(int j=0; j<m; ++j)a[i][j]=-a[i][j];
	cin>>k;
	for(int i=0; i<k; ++i){
		int x, y, d, r;
		cin>>x>>y>>d>>r;
		x=n-x+d, y=m-y+d;
		a[x][y]+=r;
	}
	int ans=0;
	for(int i=0; i<n; ++i){
		for(int j=0; j<m; ++j)dp0[j]=dp[j];
		for(int j=0; j<m; ++j)dp[j]=a[i][j]+(j?dp[j-1]:0);
		for(int j=0; j<m; ++j)dp[j]+=dp0[j];
		for(int j=m-2; j>=0; --j)dp[j]=max(dp[j], dp[j+1]);
		ans=max(ans, dp[0]);
	}
	cout<<ans<<endl;
	//for(int i=0; i<=n; ++i)sa[i][0]=0;
	//for(int i=0; i<=m; ++i)sa[0][i]=0;
	//for(int i=0; i<n; ++i)for(int j=0; j<m; ++j)sa[i+1][j+1]=a[i][j]+sa[i][j+1]+sa[i+1][j]-sa[i][j];
	
}
