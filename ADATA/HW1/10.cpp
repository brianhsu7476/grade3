#include <bits/stdc++.h>
#define int long long
#define endl '\n'
using namespace std;
#define kN 100005
#define kK 31
#define kM 11
int n, m, k, a[kN], c[kN], sa[kN][kM], cnt[kM], cnt0[kK][kM];

int walk(int x, int d){
	int g=0;
	for(int i=0; i<d; ++i)if(x>>(k-i-1)&1)g+=c[i];
	return g%m;
}

int smtree(int x, int d){
	int g=walk(x, d), ans=0;
	for(int i=0; i<m; ++i)ans+=(g+i)%m*cnt0[d+1][i];
	return ans;
}

int solve(int x){
	int y=x%n, ans=0, g;
	//cout<<"xg "<<x<<' ';
	x/=n, g=walk(x, k);
	//cout<<g<<endl;
	if(x>>k)return smtree(x, -1);
	for(int i=0; i<k; ++i)if(x>>(k-i-1)&1)ans+=smtree(x, i);
	//cout<<"ans y "<<ans<<' '<<y<<endl;
	for(int i=0; i<m; ++i)ans+=(g+i)%m*sa[y][i];
	return ans;
}

signed main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n>>m>>k;
	for(int i=0; i<n; ++i)cin>>a[i];
	for(int i=0; i<n; ++i){
		for(int j=0; j<m; ++j)sa[i+1][j]=sa[i][j];
		++sa[i+1][a[i]];
		//for(int j=0; j<m; ++j)cout<<sa[i+1][j]<<" \n"[j==m-1];
	}
	for(int i=0; i<k; ++i)cin>>c[i];
	for(int i=0; i<=k; ++i){
		cnt0[i][0]=1;
		for(int j=i; j<k; ++j){
			for(int l=0; l<m; ++l)cnt[l]=cnt0[i][l]+cnt0[i][(l+m-c[j])%m];
			for(int l=0; l<m; ++l)cnt0[i][l]=cnt[l];
		}
		for(int l=0; l<m; ++l)cnt[l]=cnt0[i][l], cnt0[i][l]=0;
		for(int l=0; l<m; ++l)for(int r=0; r<m; ++r)cnt0[i][(l+r)%m]+=cnt[l]*sa[n][r];
	}
	//for(int i=0; i<=(n<<k); ++i)cout<<solve(i)<<' ';
	//cout<<endl;
	int q; cin>>q;
	while(q--){
		int l, r; cin>>l>>r;
		cout<<solve(r+1)-solve(l)<<endl;
	}
}
