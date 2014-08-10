#include <iostream>
#include <cstring>

using namespace std;

#define MAX_CHARS 80

inline void read_req(int nr_req) {
  for (int i = 0; i < nr_req; i++)
    cin.ignore(MAX_CHARS, '\n');
}

int main() {
  int r = 0;
  int nr_req, nr_proposal;
  int nr_met_req;
  float price, compliance;
  float best_price, best_compliance;
  char proposal[MAX_CHARS + 1];
  char best_proposal[MAX_CHARS + 1];


  while (cin >> nr_req >> nr_proposal) {
    
    if (!nr_req && !nr_proposal) break;

    cin.ignore();  // ignore newline in buffer
    read_req(nr_req);

    best_price = best_compliance = -1;
    for (int i = 0; i < nr_proposal; i++) {

      cin.getline(proposal, MAX_CHARS);
      cin >> price >> nr_met_req;

      compliance = (float) nr_met_req / nr_req;
      if (compliance > best_compliance 
	  || (compliance == best_compliance && price < best_price)) {
	best_price = price;
	strcpy(best_proposal, proposal);
	best_compliance = compliance;
      }

      cin.ignore();
      read_req(nr_met_req);
    }

    if (r) cout << "\n";
    cout << "RFP #" << ++r << "\n" << best_proposal << "\n";
  }
  return 0;
}
