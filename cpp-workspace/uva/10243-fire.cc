
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

#define MAX_NODES 1000

struct graph
{
  const int V;
  vector<vector<int> > adj;

  graph(int V) : V(V), adj(V) {}

  void add_edge(int u, int v) {
    adj[u].push_back(v);
  }
};

struct visitor
{
  virtual void visit(int) = 0;
};

struct search
{
  bool visited[MAX_NODES];
  
  void dfs(graph& G, int root, visitor& vis) {
    stack<int> nodes;
    fill_n(visited, G.V, false);
    nodes.push(root);
    visited[root] = true;

    while(!nodes.empty()) {
      int u = nodes.top();
      for (int i = 0; i < G.adj[u].size(); i++) {
	int v = G.adj[u][i];
	if (!visited[v]) nodes.push(v), visited[v] = true;
      }
      if (u == nodes.top()) nodes.pop(), vis.visit(u);
    }
  }
};

struct simple_test_visitor : public visitor
{
  void visit(int u) { cout << u << " "; }
};

struct min_vertex_cover : public visitor
{
  graph* G;
  search S;
  int covered[MAX_NODES];

  int solve(graph& G){
    // critical case: zero edges, primary algo won't work
    if (G.V == 1) return 1;  

    this->G = &G;
    fill_n(covered, G.V, -1);
    S.dfs(G, 0, *this);
    
    int count = 0;
    for (int i = 0; i < G.V; i++) count += covered[i];
    return count;
  }

  void visit(int u) {
    for (int i = 0; i < G->adj[u].size(); i++) {
      int v = G->adj[u][i];
      if (covered[v] == 0) {
	covered[u] = 1; return;
      }
    }
    covered[u] = 0;
  }
};

int main()
{
  min_vertex_cover vertex_solver;

  while(true) {
    int u, v, N, M;

    cin >> N;
    if (N == 0) break;

    graph G(N);

    for (u = 0; u < N; u++) {
      cin >> M;
      for (int j = 0; j < M; j++) {
	cin >> v;
	G.add_edge(u, v - 1);
      }
    }

    cout << vertex_solver.solve(G) << "\n";
  }

  return 0;
}
