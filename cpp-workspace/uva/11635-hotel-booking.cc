
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_DIST 600		// 600km = 10hrs = 600mins
#define MAX_HOTELS 100
#define MAX_CITIES 10000

template<class keyType> class PQ {
  int d, N;
  vector<int> pq, qp;
  const vector<keyType> &a;

  void exch(int i, int j) {
    int t = pq[i];
    pq[i] = pq[j];
    pq[j] = t;
    qp[pq[i]] = i;
    qp[pq[j]] = j;
  }

  void fixUp(int k) {
    while (k > 1 && a[pq[(k + d - 2) / d]] > a[pq[k]]) {
      exch(k, (k + d - 2) / d);
      k = (k + d - 2) / d;
    }
  }

  void fixDown(int k, int N) {
    int j;
    while ((j = d * (k - 1) + 2) <= N) {
      for (int i = j + 1; i < j + d && i <= N; i++)
	if (a[pq[j]] > a[pq[i]])
	  j = i;
      if (!(a[pq[k]] > a[pq[j]]))
	break;
      exch(k, j);
      k = j;
    }
  }

public:
  PQ(int N, const vector<keyType> &a, int d = 3) :
    a(a), pq(N + 1, 0), qp(N + 1, 0), N(0), d(d) {
  }

  int empty() const {
    return N == 0;
  }
	
  void insert(int v) {
    pq[++N] = v;
    qp[v] = N;
    fixUp(N);
  }
	
  int getmin() {
    exch(1, N);
    fixDown(1, N - 1);
    return pq[N--];
  }
	
  void lower(int k) {
    fixUp(qp[k]);
  }
};

struct edge {
  int u, v, w;
  edge(int u, int v, int w): u(u), v(v), w(w) { }
};

typedef vector<edge> T;

class graph {
  T* adjList;

public:
  graph(int);
  ~graph();
  const T& adj(int);
  void add_edge(int, int, int);
};

graph::graph(int V) {
  adjList = new T[V];
}

graph::~graph() {
  delete[]	 adjList;
}

const T& graph::adj(int v) {
  return adjList[v];
}

void graph::add_edge(int u, int v, int w) {
  adjList[u].push_back(edge(u, v, w));
  adjList[v].push_back(edge(v, u, w));
}

int neighborhood(graph& in, int n, int s, int t, int* ch, int h) {

  queue<int> neighbors;
  vector<int> dist(n);                  // dist in dijkstra iteration
  bool unvisited_h[MAX_CITIES] = { 0 };	// unvisited hotels
	
  for (int i = 0; i < h; i++)	unvisited_h[ch[i]] = true;
  neighbors.push(s);

  int len = 1;
  for (int i = 0, j = 0, k = 0; !neighbors.empty(); i++) {
    // next source vertex
    s = neighbors.front(); neighbors.pop();

    // begin: one dijkstra iteration
    fill(dist.begin(), dist.end(), MAX_DIST + 1);
    PQ<int> pq(n, dist);

    // set source vertex dist = 0
    for (int v = 0; v < n; v++) pq.insert(v);
    dist[s] = 0; pq.lower(s);

    while (!pq.empty()) {
      int u = pq.getmin();
			
      // stop if no more hotels within max hop dist
      if (dist[u] > MAX_DIST)	break;

      const T& adj = in.adj(u);
      for (T::const_iterator e = adj.begin(); e != adj.end(); ++e) {

	// order of the following conditional statements is important
	const int& v = e->v;
	int d = dist[u] + e->w;

	// avoid self-loops, only consider neighbors within MAX_DIST range
	if (u == v || s == v || d > MAX_DIST) continue;

	// if reached destination
	if (v == t)	return len;
				
	// dijkstra path relax
	if (d < dist[v]) dist[v] = d, pq.lower(v);
		
	// only consider unvisited hotels
	if (unvisited_h[v])	{
	  // update bfs variables
	  neighbors.push(v); 
	  unvisited_h[v] = false; k++;
	}
      }
    }
    if (i == j) len++, j = k;
  }

  return -1;
}

int main() {

  int n, h, m;
  int ch[MAX_HOTELS];
	
  while ((cin >> n) && n) {
    graph G(n);		
    cin >> h;
    for (int i = 0; i < h; i++)		cin >> ch[i], ch[i]--;
    cin >> m;
    for (int i = 0; i < m; i++)	{
      int u, v, w;
      cin >> u >> v >> w;
      G.add_edge(u - 1, v - 1, w);	
    }
		
    int len = neighborhood(G, n, 0, n - 1, ch, h);

    // hotels traversed = (path length from source to target) - 1
    cout <<  (len > 0 ? len - 1 : -1) << "\n";
  }

  return 0;
}

/* Input test cases:

60
6 1 2 3 40 5 6
16
1 20 55
1 30 200
20 40 500
20 30 50
20 50 800
30 40 500
30 50 401
40 60 50
40 50 50
50 60 201
1 1 1
20 20 1
30 30 1
40 40 1
50 50 1
60 60 1
6
6 1 2 3 4 5 6
10
1 2 50
1 3 200
2 4 500
2 3 50
2 5 800
3 4 500
3 5 400
4 6 500
4 5 50
5 6 1000
6
3 2 5 3
8
1 2 400
3 2 80
3 4 301
4 5 290
5 6 139
1 3 375
2 5 462
4 6 300
3
0
2
1 2 371
2 3 230
2
1 2
1
1 2 1
4
1 2
3
1 2 300
2 3 300
3 4 300
10000
1 9999
2
1 9999 600
9999 10000 600
0

*/
