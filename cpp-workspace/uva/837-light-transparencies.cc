#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;

struct ray {
  float init_pt;
  float trans;
};

bool ray_cmp(ray r1, ray r2)
{
  return r1.init_pt < r2.init_pt;
}

void solve(int nl)
{
  vector<ray> rays;
  for (int i = 0; i < nl; i++) {
    ray r1, r2;
    float t, dummy;    

    cin >> r1.init_pt >> dummy >> r2.init_pt >> dummy >> t;

    // film is transparent -> ray.trans is never zero
    t = (r1.init_pt < r2.init_pt) * t + (r1.init_pt > r2.init_pt) / t;
    r1.trans = t;
    r2.trans = 1.0 / t;
    rays.push_back(r1);
    rays.push_back(r2);
  }
  sort(rays.begin(), rays.end(), ray_cmp);

  int np = (nl << 1) + 1;
  cout << np << "\n";

  vector<ray>::iterator it = rays.begin();  
  float init_pt = it->init_pt;
  float trans = it->trans;

  cout << fixed << setprecision(3) << "-inf " << init_pt << " 1.000\n";
  for (++it; it != rays.end(); ++it) {
    cout << init_pt << " " << it->init_pt << " " << trans << "\n";
    init_pt = it->init_pt;
    trans *= it->trans;
  }
  cout << init_pt << " +inf 1.000\n";
}

int main()
{
  int n, nl;
  cin >> n;
  while (n--) {
    cin >> nl;
    solve(nl);
    if (n) cout << "\n"; 
  }
  return 0;
}
