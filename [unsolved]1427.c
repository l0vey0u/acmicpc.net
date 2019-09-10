#include <stdio.h>
int main()
{
    int tmp;
    int i = 0;
    int digit[10];
    scanf("%d", &tmp);
    if(tmp<10) {
        printf("%d\n", tmp);
        return 0;
    }
    do {
        digit[i++] = tmp%10;
        tmp /= 10;
    } while(tmp);
    
    for(tmp = 0; tmp<i; tmp++) {
        printf("%d ", digit[tmp]);
    }
    printf("\n");
    return 0;
}
