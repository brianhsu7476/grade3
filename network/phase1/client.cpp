#include <bits/stdc++.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
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
void toUpper(char *s){
	for(int i=0; s[i]; ++i)s[i]=toUpper(s[i]);
}

int main(){
	int fd=socket(AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in sif;
	sif.sin_family=AF_INET, inet_aton(host, &sif.sin_addr), sif.sin_port=htons(port);
	connect(fd, (sockaddr*)&sif, sizeof(sif));
	static char buf[kN];
	string s;
	getline(cin, s);
	for(int i=0; i<s.size(); ++i)buf[i]=s[i];
	buf[s.size()]=0;
	send(fd, buf, strlen(buf), 0);
	recv(fd, buf, sizeof(buf), 0);
	cout<<"From Server: "<<buf<<endl;
	close(fd);
}
