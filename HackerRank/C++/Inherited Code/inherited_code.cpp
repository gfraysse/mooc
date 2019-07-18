#include <iostream>
#include <string>
#include <sstream>
#include <exception>

using namespace std;

/* Define the exception here */
class BadLengthException: public std::exception {
private:
  int dN;
  char *sN;
  
public:
  BadLengthException(int n):std::exception(), dN(n) {
      sN = new char[100];
      std::string s = std::to_string(n);
      sprintf(sN, s.c_str());
  }
  
  BadLengthException(const BadLengthException &e): std::exception(e), dN(e.dN) {
      this->sN = new char[100];
      sprintf(this->sN, e.sN);
  }

  virtual ~BadLengthException() {}
  
  virtual const char* what() const noexcept  {
      return (const char *)this->sN;
  }  

};
  
// Code below is locked in HackerRank
bool checkUsername(string username) {
	bool isValid = true;
	int n = username.length();
	if(n < 5) {
		throw BadLengthException(n);
	}
	for(int i = 0; i < n-1; i++) {
		if(username[i] == 'w' && username[i+1] == 'w') {
			isValid = false;
		}
	}
	return isValid;
}

int main() {
	int T; cin >> T;
	while(T--) {
		string username;
		cin >> username;
		try {
			bool isValid = checkUsername(username);
			if(isValid) {
				cout << "Valid" << '\n';
			} else {
				cout << "Invalid" << '\n';
			}
		} catch (BadLengthException e) {
			cout << "Too short: " << e.what() << '\n';
		}
	}
	return 0;
}
