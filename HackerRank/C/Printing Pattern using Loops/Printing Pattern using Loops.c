#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int length = (2 * n) - 1;
    for (int i = 0; i < length; i++) {
      for (int j = 0; j < length; j++) {
        int dist_min = i;
        if (j < dist_min)
          dist_min = j;
        if (length - i - 1< dist_min)
          dist_min = length - i - 1;
        if (length - j - 1 < dist_min)
          dist_min = length - j - 1;
        printf("%d ", n - dist_min);
      }
      printf("\n");
    }
      return 0;
}
