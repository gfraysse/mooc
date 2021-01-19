// 
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Spell { 
    private:
        string scrollName;
    public:
        Spell(): scrollName("") { }
        Spell(string name): scrollName(name) { }
        virtual ~Spell() { }
        string revealScrollName() {
            return scrollName;
        }
};

class Fireball : public Spell { 
    private: int power;
    public:
        Fireball(int power): power(power) { }
        void revealFirepower(){
            cout << "Fireball: " << power << endl;
        }
};

class Frostbite : public Spell {
    private: int power;
    public:
        Frostbite(int power): power(power) { }
        void revealFrostpower(){
            cout << "Frostbite: " << power << endl;
        }
};

class Thunderstorm : public Spell { 
    private: int power;
    public:
        Thunderstorm(int power): power(power) { }
        void revealThunderpower(){
            cout << "Thunderstorm: " << power << endl;
        }
};

class Waterbolt : public Spell { 
    private: int power;
    public:
        Waterbolt(int power): power(power) { }
        void revealWaterpower(){
            cout << "Waterbolt: " << power << endl;
        }
};

class SpellJournal {
    public:
        static string journal;
        static string read() {
            return journal;
        }
}; 
string SpellJournal::journal = "";

// /* Returns length of longest common substring of X[0..m-1]  
//    and Y[0..n-1] */
// int LCSubStr(std::string X, std::string Y) 
// {
//     size_t m = X.length();
//     size_t n = Y.length();
    
//     // Create a table to store lengths of longest 
//     // common suffixes of substrings.   Note that 
//     // LCSuff[i][j] contains length of longest 
//     // common suffix of X[0..i-1] and Y[0..j-1].    
//     int LCSuff[m+1][n+1]; 
//     int result = 0;  // To store length of the  
//                      // longest common substring 
  
//     /* Following steps build LCSuff[m+1][n+1] in 
//         bottom up fashion. */
//     for (size_t i=0; i <= m; i++) { 
//         for (size_t j=0; j <= n; j++) {   
//             // The first row and first column  
//             // entries have no logical meaning,  
//             // they are used only for simplicity  
//             // of program 
//             if (i == 0 || j == 0) {
//                 LCSuff[i][j] = 0;
//             }
//             else if (X[i - 1] == Y[j - 1]) 
//             { 
//                 LCSuff[i][j] = LCSuff[i-1][j-1] + 1; 
//                 result = max(result, LCSuff[i][j]); 
//             } 
//             else LCSuff[i][j] = 0; 
//         } 
//     } 
//     return result; 
// }

int subseqLength(std::string s1, std::string s2) {
    int l = 0;

    size_t j = 0;
    // for(size_t j = 0; j < s2.length(); ++j) {
    while(j < s2.length()) {
        // cout << "for s2[" << j <<"]="<< s2[j] << endl;
        int last_length = 0;
        int length= 0;
        for(size_t i = 0; i < s1.length(); ++i) {
            length = 0;
            if (s2[j] == s1[i]) {
                // cout << s2[j] << s1[i] << endl;
                length ++;
                for(size_t k = i+1; k < s1.length(); ++k) {
                    // cout << "s2["<< j+k-i << "]=" << s2[j+k-i] << ", s1[" << k << "] =" << s1[k] << endl;
                    if (s2[j+k-i] == s1[k]) {
                        length ++;
                    }
                    else {
                        break;
                    }                    
                }
            }
            if (length > last_length) {
                last_length = length;
            }
            // cout << "j=" << j << ", last_length=" << last_length << ", substr=" << s2.substr(j, last_length) << endl;                
        }
        l += last_length;
        // cout << "last_length="<< last_length << ", l=" << l << endl;
        if(last_length > 1) {
            j += last_length;
        } else {
            ++j;
        }
        // cout << "j=" <<j << endl;
    }
    
    return l;
}

void counterspell(Spell *spell) {

  /* Enter your code here */
    Waterbolt *w = dynamic_cast<Waterbolt *>(spell);
    if (w != nullptr) {
        w->revealWaterpower();
    } else {
        Thunderstorm *t = dynamic_cast<Thunderstorm *>(spell);
        if (t != nullptr) {
            t->revealThunderpower();
        }
        else {
            Frostbite *fb = dynamic_cast<Frostbite *>(spell);
            if (fb != nullptr) {
                fb->revealFrostpower();
            }
            else {
                Frostbite *fb = dynamic_cast<Frostbite *>(spell);
                if (fb != nullptr) {
                    fb->revealFrostpower();
                }
                else {
                    Fireball *f = dynamic_cast<Fireball*>(spell);
                    if (f != nullptr) {
                        f->revealFirepower();
                    } else {
                        string s1= spell->revealScrollName();
                        string s2= SpellJournal::read();
                        int m = s1.length();
                        int n = s2.length();
                        int C[m+1][n+1];
                        for (int i = 0; i <= m; i++) {
                            C[i][0] = 0;
                        }
                        for (int j = 0; j <= n; j++) {
                            C[0][j] = 0;
                        }   
                        for (int i = 1; i <= m; i++) {
                            for (int j = 1; j <= n; j++) {
                                if (s1[i - 1] == s2[j - 1])
                                    C[i][j] = C[i - 1][j - 1] + 1;
                                else
                                    C[i][j] = max(C[i][j - 1], C[i - 1][j]);
                            }
                        }
                        cout << C[m][n] << endl;
                    }                    
                }
            }
        }
    }
}

class Wizard {
    public:
        Spell *cast() {
            Spell *spell;
            string s; cin >> s;
            int power; cin >> power;
            if(s == "fire") {
                spell = new Fireball(power);
            }
            else if(s == "frost") {
                spell = new Frostbite(power);
            }
            else if(s == "water") {
                spell = new Waterbolt(power);
            }
            else if(s == "thunder") {
                spell = new Thunderstorm(power);
            } 
            else {
                spell = new Spell(s);
                cin >> SpellJournal::journal;
            }
            return spell;
        }
};

int main() {
    int T;
    cin >> T;
    Wizard Arawn;
    while(T--) {
        Spell *spell = Arawn.cast();
        counterspell(spell);
    }
    return 0;
}
