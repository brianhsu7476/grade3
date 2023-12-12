#include <bits/stdc++.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <thread>
#define ushort unsigned short
#define kN 100005
using namespace std;

#ifdef brianhsu
#define green "\033[1;32m"
#define white "\033[1;0m"
#define debug(a) cerr<<green<<#a<<' '<<(a)<<white<<endl;
#else
#define debug(a) ((void)0)
#endif

const char* host="0.0.0.0";
const ushort port=8585;

char toUpper(char c){return 'a'<=c&&c<='z'?c+'A'-'a':c;}
void toUpper(char *l, char *r){
	for(char *i=l; i<r; ++i)*i=toUpper(*i);
}

string toStr(sockaddr_in cif){
	return (string)inet_ntoa(cif.sin_addr)+":"+to_string(cif.sin_port);
}

int main(){
	int fd=socket(AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in sif, cif;
	sif.sin_family=AF_INET, inet_aton(host, &sif.sin_addr), sif.sin_port=htons(port);
	bind(fd, (sockaddr*)&sif, sizeof(sif));
	listen(fd, 5);
	vector<thread> thd;
	while(1){
		socklen_t len;
		int cfd=accept(fd, (sockaddr*)&cif, &len);
		auto f=[](int cfd, string cif){
			cout<<"New client "<<cif<<endl;
			static char buf[kN];
			int n;
			while(n=recv(cfd, buf, sizeof(buf), 0)){
				buf[n]=0;
				cout<<"Receive "<<buf<<" from "<<cif<<endl;
				toUpper(buf, buf+n);
				send(cfd, buf, n, 0);
				cout<<"Send "<<buf<<" to "<<cif<<endl;
			}
			cout<<"Client "<<cif<<" leaves\n";
		};
		thd.push_back(thread(f, cfd, toStr(cif)));
	}
	close(fd);
}
