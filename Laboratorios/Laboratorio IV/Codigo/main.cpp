#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <ctime>
using namespace std;

vector<int> solucionUno(const vector<int> &A){
	vector<int> respuesta(A.size());

	


	return respuesta;
}

vector<int> solucionDos(const vector<int> &A){
	vector<int> respuesta(A.size());
	stack<int> S;



	return respuesta;
}

int main(){

	srand(time(NULL));
	int n = 10;
	vector<int> A(n);
	for(int i=0;i<n;i++)
		A[i] = rand()%1000;
	vector<int> r1 = solucionUno(A);
	vector<int> r2 = solucionDos(A);
	

}