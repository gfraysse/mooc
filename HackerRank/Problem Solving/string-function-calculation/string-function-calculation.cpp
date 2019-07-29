#include <bits/stdc++.h>

#include <cstdint>
#include <string>
#include <vector>

std::vector<std::string> getSubstrings(std::string &t) {
  std::vector<std::string> ret;
  for (size_t i = 0; i < t.length(); ++i) {
    for (size_t j = 0; j < t.length() - i; ++j) {
      std::string s = t.substr(i, j - i + 1);
      bool found = false;
      for (auto tmp : ret) {
        if (tmp == s) {
          found = true;
          break;
        }
      }
      if (found == false) {
        ret.push_back(s);
        // Heuristic: it is not possible to have more
        // substrings than the size of the string itself
        // std::cerr << "size = "<< ret.size() << std::endl;
        if (ret.size() == t.length() + 1) {
          return ret;
        }
      }
    }
  }
  return ret;
}

uint64_t f(std::string t, std::string s) {
  uint64_t ret = 0;
  for (size_t i = 0; i <= t.length() - s.length(); ++i) {
    // std::cerr << "i = "<< i << std::endl;
    if (t.substr(i, s.length()) == s) {
      ++ret;
    }
  }
  ret = ret * s.length();
  return ret;
}

// Complete the maxValue function below.
uint64_t maxValue(std::string t) {
  std::vector<std::string> substrings = getSubstrings(t);
  // std::cerr << "Found "<< substrings.size() << " substrings" << std::endl;
  uint64_t max = 0;

  for (auto s : substrings) {
    // std::cerr << s << std::endl;
    uint64_t f_val = f(t, s);
    if (f_val > max) {
      max = f_val;
    }
  }
  std::cerr << max << std::endl;
  return max;
}

int main() {
  std::ofstream fout(getenv("OUTPUT_PATH"));

  std::string t;
  // std::string t = "";
  // for (int i = 0; i < 10000; ++i) {
  //     t.append("a");
  // }
  getline(std::cin, t);

  uint64_t result = maxValue(t);

  fout << result << "\n";

  fout.close();

  return 0;
}
