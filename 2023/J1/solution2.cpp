#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <ctype.h>

using namespace std;

int get_digit(string word, map<string, int> string_digit, bool first) {

	if (first) {
		int index = 0;

		for (string::iterator it = word.begin(); it != word.end(); it++) {
			if (isdigit(*it)) {
				return *it - '0';
			}

			else {
				for (map<string, int>::iterator it2 = string_digit.begin(); it2 != string_digit.end(); it2++) {
					if (word.find(it2->first) == index) {
						return it2->second;
					}
				}
			}

			index = index + 1;

		}
	}

	else {
		int index = word.size() - 1;

		for (string::reverse_iterator it = word.rbegin(); it != word.rend(); it++) {

			if (isdigit(*it)) {
				return *it - '0';
			}

			else {
				for (map<string, int>::iterator it2 = string_digit.begin(); it2 != string_digit.end(); it2++) {
					if (word.find(it2->first, index) == index) {
						return it2->second;
					}
				}
			}

			index = index - 1;

		}
	}

	return -1;

}

int main(int argc, char* argv[]) {

	map<string, int> string_digit;

	string_digit = {
		{"one", 1},
		{"two", 2},
		{"three", 3},
		{"four", 4},
		{"five", 5},
		{"six", 6},
		{"seven", 7},
		{"eight", 8},
		{"nine", 9}
	};

	ifstream my_file;
	vector<string> data;
	string line;

	my_file.open(argv[1]);

	while (getline(my_file, line)) {
		data.push_back(line);
	}

	my_file.close();

	int first_digit;
	int last_digit;

	int result = 0;

	for (vector<string>::iterator it = data.begin(); it != data.end(); ++it) {

		first_digit = get_digit(*it, string_digit, true);
		last_digit = get_digit(*it, string_digit, false);

		result = result + 10 * first_digit + last_digit;
	}

	cout << result << "\n";

	return 0;
}