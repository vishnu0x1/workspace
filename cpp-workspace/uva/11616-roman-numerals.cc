
#include <iostream>
#include <string>

using namespace std;

char units[] = { 'I', 'X', 'C', 'M' };  // 1, 10, 100, 1000
string units_5[] = { "V", "L", "D" };  // 5, 50, 500
string units_4[] = { "IV", "XL", "CD" };  // 4, 40, 400
string units_9[] = { "IX", "XC", "CM" };  // 9, 90, 900

string convert_to_roman(string arabic)
{
  string roman;
  for (int i = 0, j = arabic.length() - 1; j >= 0; i++, j--) {
    int x = arabic[i] - '0';
    if (x == 4) {
      roman.append(units_4[j]);
    } else if (x == 5) {
      roman.append(units_5[j]);
    } else if (x == 9) {
      roman.append(units_9[j]);
    } else if (0 < x && x < 4) {
      roman.append(x, units[j]);
    } else if (5 < x & x < 9) {
      roman.append(units_5[j]);
      roman.append(x - 5, units[j]);
    }
  }
  return roman;
}

int convert_to_arabic(string roman)
{
  int arabic = 0;
  roman.append("-");  // sentinel
  for (int i = 0; i < roman.length() - 1; i++) {
    int x = roman[i]; int y = roman[i + 1];
    if (x == 'I') {
      if (y == 'V')      arabic += 4, i++;
      else if (y == 'X') arabic += 9, i++;
      else               arabic += 1;
    } 
    else if (x == 'X') {
      if (y == 'L')      arabic += 40, i++;
      else if (y == 'C') arabic += 90, i++;
      else               arabic += 10;
    } 
    else if (x == 'C') {
      if (y == 'D')      arabic += 400, i++;
      else if (y == 'M') arabic += 900, i++;
      else               arabic += 100;
    }
    else if (x == 'V')   arabic += 5;
    else if (x == 'L')   arabic += 50;
    else if (x == 'D')   arabic += 500;
    else if (x == 'M')   arabic += 1000;
  }
  return arabic;
}

int main()
{

  string line;
  while(getline(cin, line)) {
    if (line[0] >= '0' && line[0] <= '9')
      cout << convert_to_roman(line) << "\n";
    else
      cout << convert_to_arabic(line) << "\n";
  }
  return 0;
}
