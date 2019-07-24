#include <bits/stdc++.h>

using namespace std;

std::string ltrim(const std::string &);
std::string rtrim(const std::string &);
std::vector<string> split(const std::string &);

void displayMatrix(std::vector<std::vector<int>> matrix) {
    size_t rows = matrix.size();
    size_t columns = matrix[0].size();
    for (int i = 0; i < rows; i++) {
	for (int j = 0; j < columns; j++) {
	    std::cout << matrix[i][j] << " ";
	}				
	std::cout << std::endl;
    }	
}	
// Complete the matrixRotation function below.
void matrixRotation(std::vector<std::vector<int>> matrix, int r) {
    size_t rows = matrix.size();
    size_t columns = matrix[0].size();
    vector<vector<int>> matrix2;
    int r2 = r % ((rows -1) * columns);
    matrix2.resize(rows);
    
    //cout << "r2=" << r2 << endl;
    for (unsigned int r3 = 0; r3 < r2; ++r3) {
	// 3 tests were failing due to the number of iterations when
	// row /2 only was considered. min(rows,columns) / 2
	for (size_t k = 0; k < min(rows, columns) / 2; ++k) {
	    //cout << "k=" << k << endl;
	    for (size_t x = k; x < rows - k; ++x) {
		//cout << "  x=" << x << endl;	
		matrix2[x].resize(columns);
		if(x != k && x != rows - k - 1) {
		    matrix2[x][k] = matrix[x - 1][k];
		    matrix2[x][columns - k - 1] = matrix[x + 1][columns - k - 1];
		} else {
		    for (size_t y = k; y < columns - k; ++y) {
			//cout << "    y=" << y << endl;	
			if (x == k) {
			    if (y != columns - k- 1) {
				// Possible optimization don't go one
				// by one but replace 1 by number of
				// rotations as long as it is <
				// columns or rows
				matrix2[x][y] = matrix[x][y + 1];
			    } else {
				matrix2[x][y] = matrix[x + 1][y];			
			    }
			} else if (x == rows - k - 1) {
			    if (y != k) {
				matrix2[x][y] = matrix[x][y - 1];
			    } else {
				matrix2[x][y] = matrix[x - 1][y];			
			    }
			} 
		    }
		}
	    }
	}
	
	matrix = matrix2;
	// displayMatrix(matrix);
    }

    displayMatrix(matrix);

}

int main()
{
    string mnr_temp;
    getline(cin, mnr_temp);

    vector<string> mnr = split(rtrim(mnr_temp));

    int m = stoi(mnr[0]);

    int n = stoi(mnr[1]);

    int r = stoi(mnr[2]);

    vector<vector<int>> matrix(m);

    for (int i = 0; i < m; i++) {
        matrix[i].resize(n);

        string matrix_row_temp_temp;
        getline(cin, matrix_row_temp_temp);

        vector<string> matrix_row_temp = split(rtrim(matrix_row_temp_temp));

        for (int j = 0; j < n; j++) {
            int matrix_row_item = stoi(matrix_row_temp[j]);

            matrix[i][j] = matrix_row_item;
        }
    }

    matrixRotation(matrix, r);

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
