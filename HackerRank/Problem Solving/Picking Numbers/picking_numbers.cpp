#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'pickingNumbers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */
void displayVector(vector<int> a) {
#if 0
    cerr << "a=";
    for (auto &j:a){
     	cerr << j << ",";
    }
    cerr << endl;
#endif
}

int pickingNumbers(vector<int> a) {
    int previous = 0;
    int size_max = 0;
    vector<int> v;
    sort(a.begin(), a.end());

    displayVector(a);
    
    for (auto &i: a) {
	// cerr << "i=" << i << endl;
	if (previous != 0 &&  i - previous <= 1) {
	    if (v.size() != 0 && i - v[0] > 1) {
		if (v.size() > size_max ) {
		    size_max = v.size();
		}
		vector<int>::iterator itr = v.begin();
		vector<int>::iterator previous_itr = v.begin();
		for (; itr != v.end(); itr ++) {
		    if (i - (*itr) <= 1) {
			break;
		    }
		    previous_itr = itr;
		}
		v.erase(v.begin(), itr);
	    }
	    v.push_back(i);
	    displayVector(v);
	} else if (i - previous > 1) {
	    if (v.size() > size_max ) {
		size_max = v.size();
	    }
	    v.clear();
	    v.push_back(i);
	    displayVector(v);
	} else if (previous == 0) {
	     v.push_back(i);
	}
	
	previous = i;	    
    }
    if (size_max == 0) {
	size_max = v.size();
    }
    // cerr << size_max << endl;
    return size_max;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    int result = pickingNumbers(a);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
