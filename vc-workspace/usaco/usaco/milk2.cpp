/*
ID: vishnus2
LANG: C++
PROG: milk2
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define NODEBUG		// <change>

struct interval {
	int start, finish;

	interval() : start(0), finish(0) {}

	friend istream& operator>>(istream& in, interval& t) {
		in >> t.start >> t.finish;
		return in;
	}

	bool operator<(const interval& other) const {
		return start < other.start;
	}
};

int main() {

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("milk2.in");	// <change>
	ofstream fout("milk2.out");	// <change>
#endif
	vector<interval> time;
	
	int N;
	fin >> N;	
	for (int i = 0; i < N; i++) {
		interval t;
		fin >> t;
		time.push_back(t);
	}

	sort(time.begin(), time.end());

	int working, idle;
	interval curr = time[0];
	working = time[0].finish - time[0].start;
	idle = 0;
	
	for (int i = 1; i < N; i++) {
		if (time[i].start > curr.finish) {
			curr.start = time[i].start;
			idle = max(idle, time[i].start - curr.finish);
		}
		curr.finish = max(curr.finish, time[i].finish);
		working = max(working, curr.finish - curr.start);
	}

	fout << working << " " << idle << "\n";

	return EXIT_SUCCESS;
}