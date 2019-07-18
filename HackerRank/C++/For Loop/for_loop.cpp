#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    // You will be given two positive integers, a and b  (a <= b),
    // separated by a newline.
    int a, b;
    std::string s[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    scanf("%d", &a);
    scanf("%d", &b);
    for (int i = a; i <= b; ++i) {
	if (i <= 9) {
	    printf("%s\n", s[i].c_str());
	} else {
	    if (i % 2 == 0) {
		printf("even\n");
	    }
	    else {
		printf("odd\n");
	    }	    
	}
    }
    
    return 0;
}

