/*
ID: vishnus2
LANG: C++
PROG: gift1
*/

#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

using namespace std;

#define DEBUG		// <change>

typedef unordered_map<string, int> stringmap;

int main() {

#ifdef DEBUG
	ifstream fin(stdin);
	ofstream fout(stdout);	
#else
	ifstream fin("gift1.in");	// <change>
	ofstream fout("gift1.out");	// <change>
#endif

	int np;
	string* names;
	stringmap gain;

	fin >> np;
	names = new string[np];
	for (int i = 0; i < np; i++) {
		string name;
		fin >> name;
		names[i] = name;
		gain[name] = 0;
	}

	for (int i = 0; i < np; i++) {
		string giver;
		int initial;
		int ng;
		fin >> giver >> initial >> ng;

		// gain = final_amt - initial_amt
		// initial amt = (amt of money to be divided) - (leftover after dividing among members)
		gain[giver] -= initial - (ng ? initial % ng : 0);
		for (int i = 0; i < ng; i++) {
			string recepient;
			fin >> recepient;
			gain[recepient] += initial / ng;
		}
	}

	for (int i = 0; i < np; i++)
		fout << names[i] << " " << gain[names[i]] << endl;

	return 0;
}
