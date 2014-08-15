/*
ID: vishnus2
LANG: C++
PROG: palsquare
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

ifstream fin("palsquare.in");
ofstream fout("palsquare.out");

string convert2base(int num, int base)
{
    ostringstream oss;
    while (num) {
        int digit = num % base;
        oss << char(digit % 10 + (digit > 9 ? 'A' : '0'));
        num /= base;
    }
    const string& res = oss.str();
    return string(res.rbegin(), res.rend());
}

bool palindrome(string& str)
{
    return str == string(str.rbegin(), str.rend());
}

int main()
{
    int base;
    fin >> base;

    for (int i = 1; i <= 300; i++) {
        string num = convert2base(i, base);
        string square = convert2base(i * i, base);
        if (palindrome(square))
            fout << num << " " << square << "\n";
    }

    return EXIT_SUCCESS;
}
