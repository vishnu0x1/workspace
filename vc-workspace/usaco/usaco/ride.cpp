/*
ID: vishnus2
LANG: C++
PROG: ride
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//#define DEBUG

int computeScore(string);

int main() {

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("ride.in");
	ofstream fout("ride.out");
#endif
			
	string comet_name;
	string group_name;

	fin >> comet_name >> group_name;

	int cometScore = computeScore(comet_name);
	int groupScore = computeScore(group_name);

	if (cometScore == groupScore)
		fout << "GO\n";
	else
		fout << "STAY\n";

	return 0;
}

int computeScore(string str) {
	int result = str.size() > 0;
	for (string::size_type i = 0; i < str.size(); i++) {
		result *= str[i] - 'A' + 1;
	}
	return result % 47;
}