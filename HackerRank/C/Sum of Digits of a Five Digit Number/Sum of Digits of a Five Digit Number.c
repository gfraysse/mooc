#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int i = n;
    int sum = 0;
    while (i >= 10) {
      sum += i % 10;
      i = i / 10;
    }
    sum += i;
    printf("%d", sum);

    return 0;
}
