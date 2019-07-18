#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    /* The first line contains two space-separated integers denoting
       the respective values of n (the number of variable-length
       arrays) and q (the number of queries). 

       Each line i of the n subsequent lines contains a space-separated
       sequence in the format k a[i]0 a[i]1 … a[i]k-1 describing the k-element
       array located at a[i]. 

       Each of the subsequent lines contains two space-separated integers
       describing the respective values of i (an index in array a) and j (an
       index in the array referenced by a[i]) for a query.
    */
    typedef std::vector<int> line;
    
    int n, q;
    std::cin >> n >> q;
    std::vector<line> lines;

    // std::cout << "n=" << n << ", q=" << q << std::endl;
    for (int i = 0; i < n; ++i) {
	// std::cout << "i = " << i << std::endl;
	int k;
	
	std::cin >> k;
	line l;
	for (int j = 0; j < k; ++j) {
	    // std::cout << "j = " << j << std::endl;
	    int a;
	    std::cin >> a;
	    l.push_back(a);
	}
	lines.push_back(l);
    }
    for (int i = 0; i < q; ++i) {
	int k, l;
	std::cin >> k >> l;
	std::cout << lines[k][l] << std::endl;
    }
    
    return 0;
}

