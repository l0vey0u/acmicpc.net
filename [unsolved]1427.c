#include <stdio.h>
int main()
{
    int tmp, n;
    int i = 0;
    int j;
    int head, tail;
    int minIdx, maxIdx;
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
    // dual selection sort
    head = 0;
    tail = i-1;
    while(head <= tail) {
        minIdx = head;
        maxIdx = tail;
        for(j = head; j <= tail; j++) {
            if(digit[j] < digit[minIdx])
                minIdx = j;
            if(digit[j] > digit[maxIdx])
                maxIdx = j;
        }
        tmp = digit[head];
        digit[head++] = digit[minIdx];
        digit[minIdx] = tmp;
        tmp = digit[tail];
        digit[tail--] = digit[maxIdx];
        digit[maxIdx] = tmp;
    }
    tmp = 1;
    n = 0;
    for(j=0; j<i; j++) {
        n += tmp * digit[j];
        tmp *= 10;
    }
    printf("%d\n", n);
    return 0;
}
