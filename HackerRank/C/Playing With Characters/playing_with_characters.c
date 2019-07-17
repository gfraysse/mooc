#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int MAX_LEN = 5000;
    char ch;
    char s[501];
    char sen[MAX_LEN];
    scanf("%c", &ch);
    scanf("%500s", s);
    scanf("\n");
    scanf("%4999[^\n]%*c", sen);
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);
    
    return 0;
}


