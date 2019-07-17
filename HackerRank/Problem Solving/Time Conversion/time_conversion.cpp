#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    /*
     * Write your code here.
     */
     string ret = "";
if (s.find("PM") != string::npos) {
    ret = s.substr(0, s.length()-2);
int hour = atoi(s.substr(0,2).c_str());
hour+=12;
if (hour ==12) {
    hour=0;
    ret[0] = '0';
    ret[1] = '0';
} else if(hour==24) {
   ret[0] = '1';
    ret[1] = '2';

} else {
string hour_s = std::to_string(hour);
ret[0]=hour_s[0];
ret[1]=hour_s[1];
}
}
 else {
     ret = s.substr(0, s.length()-2);
int hour = atoi(s.substr(0,2).c_str());
if (hour ==12) {
    ret[0] = '0';
    ret[1] = '0';
}

}

return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

