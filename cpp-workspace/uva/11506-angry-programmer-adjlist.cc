
#include <queue>
#include <vector>
#include <iostream>

#define MAX_FLOW 100000 * 1000

using namespace std;

struct edge {
  int v, w, cap, flow, index;
  edge(int v, int w, int cap, int flow, int index) 
    : v(v), w(w), cap(cap), flow(flow), index(index) {}
};

struct graph {
  vector<vector<edge> > G; // gcc compilation error: `>>' should be `> >'
  vector<int> head;

  graph(int V) : G(V), head(V) {}

  edge& current(int v) {
    return G[v][head[v]];
  }

  edge& next(int v) {
    head[v] = ++head[v] % G[v].size();
    return G[v][head[v]];
  }

  edge& last(int v) {
    return G[v].back();
  }

  void add_edge(int u, int v, int cap) {
    G[u].push_back(edge(u, v, cap, 0, G[v].size()));
    if(u == v) G[u].back().index++;
    G[v].push_back(edge(v, u, 0, 0, G[u].size() - 1));
  }
};

class flow : public graph
{
  const int V;
  vector<int> excess, dist;
  vector<bool> active;
  queue<int> Q;

  void push(edge&);
  void relabel(int);
  void discharge();
  void init_preflow(int, int);

public:
  flow(int);
  int max_flow(int, int);
};

flow::flow(int V): graph(V), V(V), excess(V), dist(V), active(V) {}

void flow::push(edge &e) {
  int delta = min(excess[e.v], e.cap - e.flow);
  e.flow += delta;  G[e.w][e.index].flow -= delta;
  excess[e.v] -= delta;  excess[e.w] += delta;
}

void flow::relabel(int v) {
  int min_height =  V << 1; // max value of height = 2V - 1
  for (int i = 0; i < G[v].size(); i++) {
    edge& e = G[v][i];
    if (e.cap - e.flow > 0 && min_height > dist[e.w])
      min_height = dist[e.w];
  }
  dist[v] = 1 + min_height;
}

void flow::discharge() {
  int v = Q.front(); 
  int initial_dist = dist[v];
  
  while (excess[v] > 0 && dist[v] == initial_dist) {
    edge& e = current(v);
    if (e.cap - e.flow > 0 && dist[e.v] == dist[e.w] + 1) {
      push(e);
      if (!active[e.w] && excess[e.w] > 0)
	Q.push(e.w), active[e.w] = true;
    } else {
      if (&e == &last(v)) relabel(v);
      next(v);
    }
  }

  if (excess[v] == 0) 
    Q.pop(), active[v] = false;
}


int flow::max_flow(int s, int t) {
  init_preflow(s, t);
  while (!Q.empty()) discharge();
  return -excess[s];  // -e[s] == e[t]
}

void flow::init_preflow(int s, int t) {  
  active[s] = active[t] = true;  // disallow s, t in Q
  for (int i = 0; i < G[s].size(); i++) {
    edge& e = G[s][i];
    e.flow = e.cap;
    G[e.w][e.index].flow = -e.cap;
    excess[e.w] += e.cap;
    excess[s] -= e.cap;
    if (!active[e.w] && excess[e.w] > 0)
      Q.push(e.w), active[e.w] = true;
  }
  dist[s] = V;
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
