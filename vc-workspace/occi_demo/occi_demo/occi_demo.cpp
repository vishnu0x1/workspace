// occi_demo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace oracle::occi;
using namespace std;

typedef unsigned long ul;

void displayRows(Connection* const, string);

int main(int argc, char* argv[]) 
{
	string user;
	string pass;
	string osid;
	string sqlStmt;

	cin >> user >> pass >> osid;
	cin.ignore();
	getline(cin, sqlStmt);

	Environment* const env = Environment::createEnvironment(Environment::DEFAULT);

	int ret = 0;
	try {

		Connection* const con = env->createConnection(user, pass, osid);
		clog << "Connected as " << user << "@" << osid << "." << endl;
		displayRows(con, sqlStmt);
		clog << "Closing connection." << endl;
		env->terminateConnection(con);

	} catch (SQLException ea) {

		cerr << "Can’t connect: " << ea.what();
		ret = 1;

	}

	Environment::terminateEnvironment(env);
	return ret;
}

void displayRows(Connection* const con, string sqlStmt)
{

	const int prefetch_row_count = 10000;
	Statement* stmt;
	ul count = 0;

	try {

		stmt = con->createStatement(sqlStmt);
		stmt->setPrefetchRowCount(prefetch_row_count);
		clog << "Executing query: " << sqlStmt << endl;
		ResultSet* rs = stmt->executeQuery();
		clog << "Fetching rows..." << endl;
		while (rs->next()) {
			cout << rs->getString(1) << "\n";
			count++;
			if (count % prefetch_row_count == 0)
				clog << count << " rows processed" << endl;
		}
		clog << "Total number of rows fetched: " << count << endl;
		stmt->closeResultSet(rs);

	} catch(SQLException ex) {

		cerr << "Exception thrown for displayAllRows" << endl;
		cerr << "Error number: "<<  ex.getErrorCode() << endl;
		cerr << ex.getMessage() << endl;

	}

	con->terminateStatement(stmt);
}