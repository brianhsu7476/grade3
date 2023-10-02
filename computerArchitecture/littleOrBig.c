#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <stdlib.h>
#define ENDIAN_CHECK \
({ \
int _a = 1; \
char *_p = (char *)&_a; \
*_p; \
})
#define S1 "Little Endian"
#define S2 "Big Endian"
int main(void)
{
	//long long a=0xdeadbeaf;
	//uint32_t b=a, c=*((int*)&a+1), d=a>>32;
	//printf("%lld %u %u %u\n", a, b, c, d);
	char s[32];
	int a=INT_MIN;
	sprintf(s, "%d\n", a);
	printf("%s\n", s[0]=='-'?s+1:s);
	if (ENDIAN_CHECK)
		printf(S1 "\n");
	else
		printf(S2 "\n");
	return 0;
}
