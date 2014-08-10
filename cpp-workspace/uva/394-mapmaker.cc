#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;

struct array {
  string name;
  int base_addr;
  int element_size;
  int nr_dim;
  int* lower_bound;
  int* upper_bound;
  int* constants;
  
  void calc_constants() {
    constants = new int[nr_dim + 1];
    constants[nr_dim] = element_size;
    constants[0] = base_addr - constants[nr_dim] * lower_bound[nr_dim];
    for (int i = nr_dim-1; i > 0; i--) {
      constants[i] = constants[i+1] * (upper_bound[i+1] - lower_bound[i+1] + 1);
      constants[0] -= constants[i] * lower_bound[i];
    }
  }
  
  void print_physical_addr(int* array_indices) {
    int physical_addr = constants[0];
    for (int i = 1; i <= nr_dim; i++) 
      physical_addr += constants[i] * array_indices[i];
    cout << name << "[";
    for (int i = 1; i <= nr_dim; i++) {
      if (i > 1)    cout << ", ";
      cout << array_indices[i];
    }
    cout << "] = " << physical_addr << "\n";
  }
    
};

int main() {
  int N, R;
  map<string, array> arrays;
  
  cin >> N >> R;
  
  for (int i = 0; i < N; i++) {
    array arr;
    cin >> arr.name >> arr.base_addr >> arr.element_size >> arr.nr_dim;
    arr.lower_bound = new int[arr.nr_dim + 1];
    arr.upper_bound = new int[arr.nr_dim + 1];
    for (int j = 1; j <= arr.nr_dim; j++)
      cin >> arr.lower_bound[j] >> arr.upper_bound[j];
    arr.calc_constants();
    arrays[arr.name] = arr;
  }
  
  for (int i = 0; i < R; i++) {
    string name;
    cin >> name;
    array& arr = arrays[name];
    int* a = new int[arr.nr_dim + 1];
    for (int j = 1; j <= arr.nr_dim; j++) 
      cin >> a[j];
    arr.print_physical_addr(a);
  }
  
  return 0;
}

