#include <bits/stdc++.h>
#define lld long long
#define endl '\n'
#define kN 300005
#define oo 1000000007
using namespace std;

struct edge{
	int v, w;
	edge(){}
	edge(int v, int w):v(v), w(w){}
	bool operator<(const edge r)const{return w>r.w||w==r.w&&v<r.v;}
};

int n, m, s, t, dis[kN], dit[kN];
lld cs[kN], ct[kN], st[kN];
bool vis[kN];
vector<int> G[kN], rG[kN];
priority_queue<edge> pq;

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n>>m>>s>>t, --s, --t;
	for(int i=0; i<n; ++i)dis[i]=dit[i]=n;
	for(int i=0; i<m; ++i){
		int u, v; cin>>u>>v, --u, --v;
		G[u].push_back(v), rG[v].push_back(u);
	}
	pq.push(edge(s, 0)), dis[s]=0;
	while(!pq.empty()){
		edge p=pq.top(); pq.pop();
		if(vis[p.v])continue;
		vis[p.v]=1;
		for(int u:G[p.v])if(dis[p.v]+1<dis[u])pq.push(edge(u, dis[u]=dis[p.v]+1));
	}
	for(int i=0; i<n; ++i)vis[i]=0;
	pq.push(edge(t, 0)), dit[t]=0;
	while(!pq.empty()){
		edge p=pq.top(); pq.pop();
		if(vis[p.v])continue;
		vis[p.v]=1;
		for(int u:rG[p.v])if(dit[p.v]+1<dit[u])pq.push(edge(u, dit[u]=dit[p.v]+1));
	}
	for(int i=0; i<n; ++i)++cs[dis[i]], ++ct[dit[i]];
	//for(int i=0; i<n; ++i)cout<<cs[i]<<" \n"[i==n-1];
	//for(int i=0; i<n; ++i)cout<<ct[i]<<" \n"[i==n-1];
	st[0]=0;
	for(int i=0; i<=n; ++i)st[i+1]=st[i]+ct[i];
	int tt=dis[t];
	if(dis[t]==n)tt=oo;
	lld ans=0;
	for(int i=0; i<n; ++i)ans+=cs[i]*st[min(max(tt-i-1, 0), n)];
	cout<<(lld)n*n-ans-m<<endl;
}
