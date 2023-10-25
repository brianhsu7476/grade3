#include <bits/stdc++.h>
#define lld long long
#define endl '\n'
using namespace std;
#define kN 1000006

int n, a[kN], b[kN], id[kN];
lld p[kN], s[kN];

void solve(){
	cin>>n;
	for(int i=0; i<n; ++i)cin>>a[i], id[i]=i, b[i]=0;
	p[0]=s[n-1]=0;
	for(int i=0; i<n-1; ++i)p[i+1]=p[i]+a[i];
	for(int i=n-2; i>=0; --i)s[i]=s[i+1]+a[i];
	for(int i=0; i<n; ++i)p[i]-=s[i];
	sort(id, id+n, [](int i, int j){return p[i]<p[j];});
	for(int i=0; i<(n>>1); ++i)b[id[i]]=1, b[id[n-1-i]]=-1;
	lld ans=0;
	int now=0;
	for(int i=0; i<n-1; ++i)now+=b[i], ans+=(lld)a[i]*now;
	cout<<ans<<endl;
}

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	int T; cin>>T;
	while(T--)solve();
}
