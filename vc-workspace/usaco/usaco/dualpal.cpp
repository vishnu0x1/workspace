/*
ID: vishnus2
LANG: C++
PROG: dualpal
*/

#include <iostream>
#include <fstream>
#include <sstream>

#define DIGITS "0123456789ABCDEFGHIJ"

using namespace std;

ifstream fin("dualpal.in");
ofstream fout("dualpal.out");

/* inefficient version, for eff implementation see palsquare.cpp */
string convert2base(int num, int base)
{
    if (!num) 
        return "";
    else
        return convert2base(num / base, base) + DIGITS[num % base];
}

bool palindrome(const string& str)
{
    return str == string(str.rbegin(), str.rend());
}

int main()
{
    int count, low;
    fin >> count >> low;  // (count, low) = (N, S)

    for (int i = low + 1; count; i++) {
        for (int base = 2; base <= 10; base++) {
            if (palindrome(convert2base(i, base))) {
                for (base++; base <= 10; base++) {
                    if (palindrome(convert2base(i, base))) {
                        fout << i << "\n";
                        count--;
                        break;
                    }                    
                }
                break;
            }
        }
    }

    return EXIT_SUCCESS;
}