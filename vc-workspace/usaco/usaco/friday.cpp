/*
ID: vishnus2
LANG: C++
PROG: friday
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define START_YEAR 1900
//#define DEBUG		// <change>

int g(int, int, int);

int main() {

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("friday.in");	// <change>
	ofstream fout("friday.out");	// <change>
#endif

	int N;
	int days_of_week[7] = { 0 };
	fin >> N;

	for (int y = START_YEAR; y < START_YEAR + N; y++) {
		for (int m = 0; m < 12; m++) {
			int d = g(y, m, 13);
			days_of_week[(d + 4) % 7]++;
		}
	}

	for (int i = 0; i < 7; i++) {
		if (i > 0) fout << " ";
		fout << days_of_week[i];
	}
	fout << endl;

	return EXIT_SUCCESS;
}

inline int g(int y, int m, int d) {
	m = (m + 9) % 12;	// rotate months: mar comes 1st, jan & feb last
	y -= m / 10;		// due to rotation, reduce 1yr, if m is jan or feb
	return (365 * y) + (y / 4) - (y / 100) + (y / 400) + (m * 306 + 5) / 10 + (d - 1);
}
