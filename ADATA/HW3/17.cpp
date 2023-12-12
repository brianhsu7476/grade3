#include <bits/stdc++.h>
#define lld long long
#define endl '\n'
#define kN 300005
#define oo 1000000000000000018
using namespace std;

struct edge{
	int v, id;
	lld w;
	edge(){}
	edge(int v, lld w, int id):v(v), w(w), id(id){};
	bool operator<(const edge r)const{return w>r.w||w==r.w&&id<r.id;}
};

int n, m, from[kN];
vector<edge> G[kN], T[kN];
priority_queue<edge> pq;
bool vis[kN], used[kN];
lld dis[kN];

void dfs(int x, int p, int f){
	if(!p)from[x]=x;
	else from[x]=f;
	for(edge e:T[x])if(e.v!=p)dfs(e.v, x, from[x]);
}

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n>>m;
	for(int i=0; i<n; ++i)dis[i]=oo;
	for(int i=0; i<m; ++i){
		int u, v, w; cin>>u>>v>>w, --u, --v;
		G[u].push_back(edge(v, w, i)), G[v].push_back(edge(u, w, i));
	}
	pq.push(edge(0, 0, -1)), dis[0]=0;
	while(!pq.empty()){
		edge p=pq.top(); pq.pop();
		if(vis[p.v])continue;
		vis[p.v]=1;
		if(~p.id)used[p.id]=1;
		for(edge e:G[p.v])if(dis[p.v]+e.w<dis[e.v])pq.push(edge(e.v, dis[e.v]=dis[p.v]+e.w, e.id));
	}
	for(int i=0; i<n; ++i)for(edge e:G[i])if(used[e.id])T[i].push_back(e);
	dfs(0, -1, -1);
	//for(int i=0; i<n; ++i)cout<<from[i]<<" \n"[i==n-1];
	//for(int i=0; i<n; ++i)cout<<dis[i]<<" \n"[i==n-1];
	lld ans=oo;
	for(int i=0; i<n; ++i)for(edge e:G[i])if(!used[e.id]&&from[i]!=from[e.v])ans=min(ans, dis[i]+dis[e.v]+e.w);
	cout<<ans<<endl;
}
