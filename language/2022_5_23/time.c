#include <time.h>
#include <stdio.h>
int main()
{
    time_t t1 = clock();
    int i = 0;
    int sum = 0;
    for(; i < 100000000; i++)
        sum++;
    time_t t2 = clock();
    printf("%ld\n", (t2 - t1));
    return 0;
}

