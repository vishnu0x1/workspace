/*
ID: vishnus2
LANG: C++
PROG: transform
*/

#include <iostream>
#include <fstream>

#define MAXN 10

using namespace std;

typedef char T;

ifstream fin("transform.in");
ofstream fout("transform.out");

struct transform {
	int N;
	T (*f)[MAXN];	// expected result
	T (*a)[MAXN];	// computed result
	T (*b)[MAXN];	// temp var

	transform(int N) : N(N), f(tf), a(ta), b(tb) {}

 	void rotate90();
	void lateral_invert();
	bool equal();

private:
	void swap();
	T tf[MAXN][MAXN];
	T ta[MAXN][MAXN];
	T tb[MAXN][MAXN];
};

void transform::rotate90()
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			b[j][N - i - 1] = a[i][j];
	}
	swap();	// swap result back to a
}

void transform::lateral_invert()
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			b[i][N - j - 1] = a[i][j];
	}
	swap(); // swap result back to a
}

bool transform::equal()
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			if (a[i][j] != f[i][j])	return false;
	}
	return true;
}

void transform::swap()
{
	T (*t)[MAXN] = a;
	a = b;
	b = t;
}


void read_matrix(T a[][MAXN], int N)
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			fin >> a[i][j];
	}
}

int main()
{
	int N;
	fin >> N;

	transform trans(N);

	read_matrix(trans.a, N);
	read_matrix(trans.f, N);

	if (trans.rotate90(), trans.equal())
		fout << "1\n";
	else if (trans.rotate90(), trans.equal())
		fout << "2\n";
	else if (trans.rotate90(), trans.equal())
		fout << "3\n";
	else if (trans.rotate90(), trans.lateral_invert(), trans.equal())
		fout << "4\n";
	else if (trans.rotate90(), trans.equal() 
		|| (trans.rotate90(), trans.equal())
		|| (trans.rotate90(), trans.equal()))
		fout << "5\n";
	else if (trans.rotate90(), trans.lateral_invert(), trans.equal())
		fout << "6\n";
	else
		fout << "7\n";
	
	return EXIT_SUCCESS;
}