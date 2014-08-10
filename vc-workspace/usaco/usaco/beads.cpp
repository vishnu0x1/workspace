/*
ID: vishnus2
LANG: C++
PROG: beads
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define DEBUG		// <change>

int main() {

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("beads.in");	// <change>
	ofstream fout("beads.out");	// <change>
#endif

	int N;
	string beads;
	int count, prev_count, max_count, white_count;
	char bead_type = 0;
	
	fin >> N;
	fin >> beads;
	
	count = prev_count = max_count = white_count = 0;

	for (int j = 0; j < 2 * N; j++) {
		int i = j % N;
		if (beads[i] == 'w') {
			white_count++;
		} else if (bead_type == beads[i]) {
			count += white_count + 1;
			white_count = 0;
		} else {
			prev_count = count;
			count = white_count + 1;
			white_count = 0;
			bead_type = beads[i];
		}
		int t = prev_count + count + white_count;
		if (max_count < t && t <= N)	max_count = t;
	}

	fout << max_count << endl;
	return 0;
}