#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>

int main(){
	int a=INT_MIN;
	bool b[14]={
		abs(a)==a, abs(a)!=a,
		a>0, a>=0, a==0, a!=0, a<=0, a<0,
		abs(a)>0, abs(a)>=0, abs(a)==0, abs(a)!=0, abs(a)<=0, abs(a)<0
	};
	for(int i=0; i<14; ++i)printf("%d%c", b[i], " \n"[i==13]);
}
