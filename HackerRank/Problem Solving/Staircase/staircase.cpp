#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
for (int i = 1; i < n+1; ++i) {
    for (int j = 0; j < n-i; ++j) {
        cout << " ";
    }
    for (int j = 0; j < i; ++j) {
    cout << "#";
    }
    cout << endl;
}

}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}

