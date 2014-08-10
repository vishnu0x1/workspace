
#include <list>
#include <iostream>
#include <cstdio>

#define MAX_FLOW 100000 * 1000

using namespace std;

class flow
{
public:
  const int V;
  int** c;
  int** f;
  int* h;  // height function
  int* e;  // excess

  void push(int, int);
  void relabel(int);
  void discharge(int);
  void init();
  void init_preflow(int);

public:
  flow(int);
  ~flow();
  void add_edge(int, int, int); 
  int max_flow(int, int);
};

flow::flow(int V): V(V) {
  init();
}

flow::~flow() {
  delete[] h;
  delete[] e;

  for (int i = 0; i < V; i++) {
    delete[] f[i];
    delete[] c[i];
  }
  delete[] f;
  delete[] c;
}

void flow::add_edge(int u, int v, int c) {
  this->c[u][v] += c;
}

void flow::push(int u, int v) {
  int delta = min(e[u], c[u][v] - f[u][v]);
  f[u][v] += delta;  f[v][u] -= delta;
  e[u] -= delta;  e[v] += delta;
}

void flow::relabel(int u) {
  int min_height =  V << 1; // max value of height = 2V - 1
  for (int v = 0; v < V; v++) {
    if (c[u][v] - f[u][v] > 0 && min_height > h[v])
      min_height = h[v];
  }
  h[u] = 1 + min_height;
}

void flow::discharge(int u) {
  int v = 0;
  while(e[u] > 0) {    
    if (v == V) {
      relabel(u);
      v = 0;
    } else {
      if (c[u][v] - f[u][v] > 0 && h[u] == h[v] + 1)
	push(u, v);
      ++v;
    }
  }
}

int flow::max_flow(int s, int t) {
  init_preflow(s);
  
  list<int> q;
  list<int>::iterator q_itr;

  for (int v = 0; v < V; v++) {
    if (v != s && v != t) q.push_back(v);
  }

  q_itr = q.begin();
  while(q_itr != q.end()) {
    int u = *q_itr;
    int old_height = h[u];
    
    discharge(u);

    if (h[u] > old_height) { // ht change => relabel occured
      q.erase(q_itr);
      q.push_front(u);
      q_itr = q.begin();
    }    
    ++q_itr;
  }
  return -e[s];  // -e[s] == e[t]
}

void flow::init() {
  h = new int[V]();
  e = new int[V]();
  
  f = new int*[V];
  c = new int*[V];
  for (int i = 0; i < V; i++) {
    f[i] = new int[V]();
    c[i] = new int[V]();
  }  
}

void flow::init_preflow(int s) {  
  for (int v = 0; v < V; v++) {
    f[s][v] = c[s][v];
    f[v][s] = -c[s][v];
    e[v] = f[s][v];
    e[s] -= c[s][v];
  }
  h[s] = V;
}

int main()
{
  int M, W;
  
  while(cin >> M >> W) {

    if (M == 0 && W == 0) break;

    flow f(M << 1);  // 2M vertices, for breaking undirected graph

    // allow infinite capacity on these edges
    f.add_edge(0, M, MAX_FLOW);  
    f.add_edge(M - 1, M - 1 + M, MAX_FLOW);

    // split the node into an innode and outnode
    // innode = u, outnode = M + u
    for (int n = 0; n < M - 2; n++) {
      int i, c;
      cin >> i >> c;
      f.add_edge(i - 1, i - 1 + M, c);  // Vin -> Vout
    }

    for (int n = 0; n < W; n++) {
      int j, k, d;
      cin >> j >> k >> d;
      f.add_edge(j - 1 + M, k - 1, d);  // V1out -> V2in
      f.add_edge(k - 1 + M, j - 1, d);  // V2out -> V1in
    }

    int flow = f.max_flow(0, M - 1 + M);
    cout << flow << "\n";
  }

  return 0;
}
