/*
ID: vishnus2
LANG: C++
PROG: test
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define DEBUG		// <change>

int main() {		// <change>

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("test.in");	// <change>
	ofstream fout("test.out");	// <change>
#endif

	int a, b;
	fin >> a >> b;
	fout << a + b << endl;

	return 0;
}
