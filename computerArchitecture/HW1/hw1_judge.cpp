#include <bits/stdc++.h>
#include <unistd.h>
#include <sys/wait.h>
#define kN 1003
#define eps 1e-6
using namespace std;

char fileName[kN], out[kN], samp[kN];

void test(int a, int op, int b){
	memset(out, 0, kN);
	int pid, pip[2];
	pipe(pip);
	if(!(pid=fork())){
		dup2(pip[0], 0), dup2(pip[1], 1);
		execlp("jupiter", "jupiter", fileName, NULL);
		close(pip[0]), close(pip[1]);
		exit(0);
	}
	int n=sprintf(out, "%d\n%d\n%d\n", a, op, b);
	write(pip[1], out, n);
	waitpid(pid, NULL, 0);
	read(pip[0], out, kN);
}

int fpow(int a, int b){
	int r=1;
	for(; b; b>>=1, a*=a)if(b&1)r*=a;
	return r;
}

int fact(int a){
	int r=1;
	for(int i=1; i<=a; ++i)r*=i;
	return r;
}

void gen(int a, int op, int b){
	memset(samp, 0, kN);
	char *out="\n\nJupiter: exit(0)\n", *div0="division by zero";
	int ans=0;
	if(op==0)ans=a+b;
	if(op==1)ans=a-b;
	if(op==2)ans=a*b;
	if(op==3&&b)ans=a/b;
	if(op==4)ans=min(a, b);
	if(op==5)ans=fpow(a, b);
	if(op==6)ans=fact(a);
	if(op==3&&!b)sprintf(samp, "%s%s", div0, out);
	else sprintf(samp, "%d%s", ans, out);
}

bool judge(int a, int op, int b){
	test(a, op, b), gen(a, op, b);
	for(int i=0; out[i]; ++i){
		if(out[i]!=samp[i]){
			printf("\033[1;33m%d %d %d\n\033[1;31m%s\n\033[1;32m%s\n", a, op, b, out, samp);
			printf("\033[1;0m");
			return 0;
		}
	}
	printf("%d %d %d correct\n", a, op, b);
	return 1;
}

signed main(int argc, char **argv){
	if(argc!=3){
		fprintf(stderr, "usage: ./judge fileName numberOfTest\n");
		exit(1);
	}
	int T=atoi(argv[2]);
	for(int i=0; argv[1][i]; ++i)fileName[i]=argv[1][i];
	while(T--){
		int a=rand()%1024, b=rand()%1024, op=rand()%7;
		if(op==3&&rand()%4==0)b=0;
		if(op==5){
			if(rand()%3==0)a=rand()%10;
			double pw=log(1e31)/log(a);
			b=pw-eps;
			b=rand()%(b+1);
		}
		if(op==6)a=rand()%13, b=0;
		judge(a, op, b);
	}
}
