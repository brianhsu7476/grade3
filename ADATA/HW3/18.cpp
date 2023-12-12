#include <bits/stdc++.h>
#define endl '\n'
#define kN 1000006
using namespace std;

/*struct P{
	int x, y;
	P(){}
	P(int x, int y):x(x), y(y){}
	bool operator<(const P r)const{return x>r.x||x==r.x&&y<r.y;}
};*/

int n, m, ord[kN], cnt, p[kN], scc[kN], sz[kN], ideg[kN], ans[kN];
vector<int> G[kN], rG[kN], H[kN];
queue<int> dag;
bool vis[kN];

void dfs0(int x, int p){
	vis[x]=1;
	for(int u:G[x])if(!vis[u])dfs0(u, x);
	ord[x]=cnt++;
}

void dfs1(int x, int p){
	scc[x]=~p?scc[p]:x, vis[x]=1, ++sz[scc[x]];
	for(int u:rG[x])if(!vis[u])dfs1(u, x);
}

int main(){
	ios::sync_with_stdio(0), cin.tie(0);
	cin>>n>>m;
	for(int i=0; i<m; ++i){
		int u, v; cin>>u>>v, --u, --v;
		G[u].push_back(v), rG[v].push_back(u);
	}
	for(int i=0; i<n; ++i)if(!vis[i])dfs0(i, -1);
	for(int i=0; i<n; ++i)p[i]=i, vis[i]=0;
	//for(int i=0; i<n; ++i)cout<<ord[i]<<" \n"[i==n-1];
	sort(p, p+n, [](int u, int v){return ord[u]>ord[v];});
	for(int i=0; i<n; ++i)if(!vis[p[i]])dfs1(p[i], -1);
	//for(int i=0; i<n; ++i)cout<<scc[i]<<" \n"[i==n-1];
	for(int i=0; i<n; ++i)ideg[i]=0;
	for(int i=0; i<n; ++i)for(int u:G[i])if(scc[i]!=scc[u])H[scc[i]].push_back(scc[u]), ++ideg[scc[u]];
	for(int i=0; i<n; ++i)if(!ideg[i]&&sz[i])dag.push(i);
	//for(int i=0; i<n; ++i)cout<<ideg[i]<<" \n"[i==n-1];
	while(!dag.empty()){
		int x=dag.front(); dag.pop();
		ans[x]+=sz[x];
		//cout<<x<<endl;
		for(int u:H[x]){
			ans[u]=max(ans[u], ans[x]);
			if(!--ideg[u])dag.push(u);
		}
	}
	int mx=0;
	//for(int i=0; i<n; ++i)cout<<ans[i]<<" \n"[i==n-1];
	for(int i=0; i<n; ++i)mx=max(mx, ans[i]);
	cout<<mx<<endl;
}
