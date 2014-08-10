
#include <iostream>
#include <string>

#define NR_KEYS 12

using namespace std;

string notes[] = { 
  "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"
};

int pos[] = { 11, 9, 8, 6, 4, 3, 1 };

int major_scale_tones[NR_KEYS];

void init_tones()
{
  int tones = 0b101011010101;  // start with a major scale
  for (int i = 0; i < NR_KEYS; i++) { // 12 semi-tones excluding octave
    major_scale_tones[i] = tones;
    // rotate one step right to obtain tones in major scale of next note
    tones = (tones >> 1) | ((tones & 1) << NR_KEYS - 1);
  }
}

int solve(int tones) {
  bool key_found = false;
  for (int i = 0; i < NR_KEYS; i++) {
    int j = (i + 3) % NR_KEYS;  // start scan from key C
    // is tones subset of major scale
    if ((major_scale_tones[j] & tones) == tones) {  
      if (key_found)  cout << " ";
      key_found = true; cout << notes[j];
    }
  }
  cout << "\n";
}

int main()
{
  init_tones();

  string line, note;
  while (getline(cin, line)) {
    if (line == "END")  break;

    line += '\0';
    int tones = 0;
    for (int i = 0; i < line.length() - 1; i++) {
      if (line[i] != '#' && line[i] != ' ')
          tones |= 1 << (pos[line[i] - 'A'] - (line[i + 1] == '#'));
    }
    solve(tones);
  }  
  
  return 0;
}
