#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    // Input consists of the following space-separated values: int, long, char, float, and double, respectively.
    int integer = 0;
    long longint = 0;
    char c = 0;
    float decimal = 0.0;
    double longdecimal = 0.0;

    scanf ("%d %ld %c %f %lf", &integer, &longint, &c, &decimal, &longdecimal);

    printf ("%d\n", integer);
    printf ("%ld\n", longint);
    printf ("%c\n", c);
    printf ("%f\n", decimal);
    printf ("%lf\n", longdecimal);

    return 0;
}

