#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int max_and = 0;
  int max_or = 0;
  int max_xor = 0;

  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j < i; ++j) {
      int v_and = i & j;
      int v_or = i | j;
      int v_xor = i ^ j;
      if (v_and > max_and && v_and < k)
        max_and = v_and;
      if (v_or > max_or && v_or < k)
        max_or = v_or;
      if (v_xor > max_xor && v_xor < k)
        max_xor = v_xor;
    }
  }
  printf("%d\n%d\n%d\n", max_and, max_or, max_xor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
