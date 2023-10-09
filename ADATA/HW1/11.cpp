#include <bits/stdc++.h>
#define umap unordered_map
#define endl '\n'
#define x first
#define y second
#define pii pair<int, int>
#define mp make_pair
#define kN 100005
using namespace std;

umap<long long, int> S;
int n;
pii p[kN];

long long toLong(pii p){return (long long)p.x<<32|p.y;}

long long dis2(pii a, pii b){
	long long dx=a.x-b.x, dy=a.y-b.y;
	return dx*dx+dy*dy;
}

double dis(pii a, pii b){return sqrt(dis2(a, b));}

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n, ++n;
	int mn=0;
	for(int i=1; i<n; ++i)p[i].x=i, cin>>p[i].y, p[i].y+=p[i-1].y, mn=min(mn, p[i].y);
	for(int i=0; i<n; ++i)p[i].y-=mn;
	double d=dis(p[0], p[1])/2;
	while(1){
		int i=0;
		for(; i<n; ++i){
			long long q=toLong(mp(p[i].x/d, p[i].y/d));
			if(S.find(q)!=S.end()){
				d=dis(p[S[q]], p[i])/2;
				S.clear();
				break;
			}
			S[q]=i;
		}
		if(i==n)break;
	}
	long long ans=1e18;
	for(int i=0; i<n; ++i){
		pii q=mp(p[i].x/d, p[i].y/d);
		for(int j=-2; j<3; ++j)for(int k=-2; k<3; ++k)if(j||k){
			long long r=toLong(mp(q.x+j, q.y+k));
			if(S.find(r)!=S.end())ans=min(ans, dis2(p[S[r]], p[i]));
		}
	}
	cout<<ans<<endl;
}
