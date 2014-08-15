/*
ID: vishnus2
LANG: C++
PROG: namenum
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

typedef unsigned long long ull;

using namespace std;

ifstream fin("namenum.in");
ofstream fout("namenum.out");

ull key(string& name) 
{
    ull key = 0;
    for (string::iterator it = name.begin(); it != name.end(); ++it) {
        int idx = *it - 'A';
        // idx = 17 => 'Q', shift idx left by 1
        idx = 2 + (idx - (idx > 17)) / 3;
        key = (key * 10) + idx;
    }
    return key;
}

int main() 
{
    map<ull, vector<string> > dict;
    ifstream dict_in("dict.txt");
    
    string name;
    while (dict_in >> name) {
        dict[key(name)].push_back(name);
    }

    ull num;
    fin >> num;
    vector<string>& names = dict[num];
    if (names.empty())
        fout << "NONE\n";
    else {
        for (vector<string>::iterator it = names.begin();
            it != names.end(); ++it)
            fout << *it << "\n";
    }

    return EXIT_SUCCESS;
}