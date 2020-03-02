#include <bits/stdc++.h>

#include <cstdint>
#include <string>
#include <vector>

uint64_t computeMax(std::string &t) {
    uint64_t max = 0;
    for (size_t i = 0; i < t.length(); ++i) {
	std::cerr << "i = "<< i << std::endl;
	
	unsigned int current_length = t.length() - i;
	if (current_length > max) {
	    max = current_length;
	    std::cerr << "max = "<< max << std::endl;
	}
	int occurences = 1;
	int max_occurences = i + 1;
	if (i > 1 && current_length * max_occurences > max) {
	    for (size_t j = 1; j <= i; ++j) {
		std::cerr << "j = "<< j << std::endl;
		size_t k = 0;
		bool exited_loop = false;
		for (; k < t.length() - i; ++k) {
		    // std::cerr << "k = "<< k << std::endl;
		    if (t[k] != t[j + k]) {
			std::cerr << "break" << std::endl;
			exited_loop = true;
			break;
		    }	
		}
		// std::cerr << "k=" << k << " / t.length - i=" << t.length() - i << std::endl;
		if (! exited_loop) {
		    ++occurences;
		    std::cerr << "occurences = "<< occurences << std::endl;
		    // std::cerr << "str= "<< t.substr(i, t.length() - i) << std::endl;
		}
	    }
	    if (occurences * (t.length() - i) > max) {
		max = occurences * (t.length() - i);
		std::cerr << "occurences2 = "<< occurences << std::endl;
		std::cerr << "max2 = "<< max << std::endl;
	    }
	}
    }
    std::cerr << "max end = "<< max << std::endl;
    return max;    
}

std::vector<std::string> getSubstrings(std::string &t) {
  std::vector<std::string> ret;
  size_t max_i = t.length() / 2;
  
  for (size_t i = 0; i < max_i; ++i) {
      for (size_t j = 0; j < max_i - i; ++j) {
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
  uint64_t max = f(t, t);

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

  // uint64_t result = maxValue(t);
  uint64_t result = computeMax(t);

  fout << result << "\n";

  fout.close();

  return 0;
}
