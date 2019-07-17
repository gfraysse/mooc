#include <bits/stdc++.h>

using namespace std;

int roundGrade(int grade) {
  if (grade < 38)
    return grade;
  int next_multiple = (5 * ((grade / 5) + 1));
  if (next_multiple - grade < 3) {
    return next_multiple;
  }
  return grade;
}

vector<int> gradingStudents(vector<int> grades) {
  /*
   * Write your code here.
   */
  vector<int> ret;
  for (auto &g : grades) {
    ret.push_back(roundGrade(g));
  }
  return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> grades(n);

    for (int grades_itr = 0; grades_itr < n; grades_itr++) {
        int grades_item;
        cin >> grades_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        grades[grades_itr] = grades_item;
    }

    vector<int> result = gradingStudents(grades);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

