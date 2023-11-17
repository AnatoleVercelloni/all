#ifndef MAPMATRIX_HPP
#define MAPMATRIX_HPP


#include<map>
#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <fstream>
#include <cstring>

#include"vector.hpp"


using namespace std;
typedef complex<double> Cplx;

template <typename T>
class MapMatrix{	

	// using T = DataType;
	int nr;
	int nc;
	typedef tuple<int, int> NxN;
	map<NxN, T> data;
	
	public:
	
	MapMatrix<T> (const int& nr, const int& nc):nr(nr), nc(nc){}
	
	MapMatrix<T> (MapMatrix<T> &M):nr(M.nr), nc(M.nc), data(M.data){}
	
	MapMatrix<T>& operator=(const MapMatrix<T> &M){
		nr = M.nr;
		nc = M.nc;
		data = M.data;
		return *this;
	}
	
	void insert(const int& i, const int& j, const T& v){
		tuple<int, int> t = {i,j};
		auto elt = data.find(t);
		auto it = data.begin();
		if (elt==data.end()){
			data.insert(it,{t,v});
		}
		else{
			 T w = data[t]+v;
			 data.erase(t);
			 data.emplace(t,w);
		}
	}
	
	
	void replace(const int& i, const int& j, const T& v){
		tuple<int, int> t = {i,j};
		auto elt = data.find(t);
		auto it = data.begin();
		T z {};
		if (v != z){
			if (elt==data.end()){
				data.insert(it,{t,v});
			}else{
				// cout << v << endl;
				 T w = v;
				 data.erase(t);
				 data.emplace(t,w);
			}
		}else{
			data.erase(t);
		}
	}
	
	friend ostream &operator<<(ostream &o, MapMatrix<T> &M){
		for (int i =0; i<M.nr; i++){
			for (int j = 0; j< M.nc; j++){
				map<NxN, T> data = M.data;
				auto elt = data.find({i,j});
				if (elt == data.end()){
					o << "\t" << "0";
				}else{
					o << "\t" << elt->second;		
				}
			}
			o << "\n";
		}
		return o;
	}
	
	MapMatrix<T> operator+(const MapMatrix<T> &M){
		MapMatrix<T> nM = M;
		nM.nc = nc;
		nM.nr = nr;
		map<NxN, T> ndata = M.data;
		for (auto it = data.begin(); it!=data.end(); ++it){
			tuple<int, int> t = it->first;
			nM.insert(get<0>(t), get<1>(t), it->second);
		}
		return nM;
	}
	
	T operator()(int j ,int k){
		// cout << j << k << endl;
		// cout << nr << nc << endl;
		T z {};
		assert(j<nr && k<nc);
		tuple<int, int> t = {j,k};
		auto f = data.find(t);
		if (f!= data.end()){
			return f->second;
		}else{
			return z;
		}
	}
	
	MapMatrix<T> operator-(const MapMatrix<T> &M){
		MapMatrix<T> nM = M;
		nM.nc = nc;
		nM.nr = nr;
		map<NxN, T> ndata = M.data;
		for (auto it = data.begin(); it!=data.end(); ++it){
			tuple<int, int> t = it->first;
			nM.insert(get<0>(t), get<1>(t), (-1)*it->second);
		}
		return nM;
	}

	MapMatrix<T> operator*(MapMatrix<T> &M){
		assert(M.nr == nc);
		MapMatrix<T> nM(nr,M.nc);
		vector<T> ndata ;
		
		for (auto it = data.begin(); it!=data.end(); it++){
			tuple<int, int> t1 = it->first;
			int i1 = get<0>(t1);
			int j1 = get<1>(t1);
			
			for (auto jt = M.data.begin(); jt!=M.data.end(); jt++){
				tuple<int, int> t2 = jt->first;
				int i2 = get<0>(t2);
				int j2 = get<1>(t2);
				
				if (j1==i2){
					// cout << i1 << j1 << i2 << j2 << endl;
					nM.insert(i1,j2, it->second*jt->second);
					// cout << "A["<<i1<<","<<j2<<"] += "<< it->second <<"*" <<jt->second << endl;
					// cout << nM << endl;
				}
			}
		}
		return nM;
	}
	
	vector<T> operator*(const vector<T> &v){
		assert(v.size() == nc);
		vector<T> nv(nc);
		for (auto it = data.begin(); it!=data.end(); it++){
			tuple<int, int> t = it->first;
			int i = get<0>(t);
			int j = get<1>(t);
			
			nv[i]+=it->second*v[j];
					
			
		}
		return nv;
	}
	
	void operator+=(MapMatrix<T> &M){
		for (auto it = M.data.begin(); it!=M.data.end(); ++it){
			tuple<int, int> t = it->first;
			(*this).insert(get<0>(t), get<1>(t), it->second);
		}
	}
	// MapMatrix<T> LoadMapMatrix(const string& filename);
	
	friend int NbRow(const MapMatrix<T>& M){
		return M.nr;
	}
	friend int NbCol(const MapMatrix<T>& M){
		return M.nc;
	}
	
	MapMatrix<Cplx> herm(){
		//nr>=nc
		Cplx tmp;
		MapMatrix<Cplx> A(nc, nr);
		int i ,j;
		for (auto it = data.begin(); it!=data.end(); it++){
				tuple<int, int> t = it->first;
				int i = get<0>(t);
				int j = get<1>(t);
				tmp = conj(it->second);
				A.insert(j,i,tmp);
				
		}
		return A;
	}
	
	vector<T> Solve_R(const vector<T>& b){
		assert(b.size() == nr - 1);
		int k = nr - 1;
		vector<T> x(k);
		int i,j;
		// cout << "b  = " << b << endl;
		for (i = 0; i < k; i++){
			for (j = 0; j<i; j++){
				x[i] = x[i] - (*this)(i,j)*x[j];
			}
			x[i] = (x[i] + b[i])/(*this)(i,i);
		}
		return x;
	}
	
	
	
};

template <typename T>
MapMatrix<T> LoadMapMatrix(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			T v;
			int i,j;
			MapMatrix<T> M(nc, nr);
			string line;
			while (file >> i) {
				file >> j;
				file >> v;
				M.insert(i,j,v);
			}
			return M;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}
	
// template <typename T>
// vector<T> Solve (MapMatrix<T>& A, vector<T> b){
	

	
template <>
MapMatrix<Cplx> LoadMapMatrix(const string& filename){
		ifstream file(filename);
		if (file){
			int nc, nr;
			file >> nc;
			file >> nr;
			double re, im;
			int i,j;
			MapMatrix<Cplx> M(nc, nr);
			string line;
			while (file >> i) {
				file >> j;
				file >> re;
				file >> im;
				Cplx c = Cplx(re, im);
				M.insert(i,j,c);
			}
			return M;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}
	
	
void givens_ij(MapMatrix<Cplx>& R, MapMatrix<Cplx>& Q, int i, int j){
	Cplx rjj = R(j, j);
	Cplx rij = R(i, j);
	Cplx x = sqrt(rjj*rjj+rij*rij);
	Cplx c = rjj/x;
	Cplx s = rij/x;
	Cplx tmp, tmp2;
	for (int k = 0; k < NbRow(R); k++) {
		// printf("iteration %d \n", k);
		
		if (k < NbCol(R)) {
			tmp = c * R(j, k) + s * R(i , k);
			tmp2 = - s * R(j, k) + c * R(i, k);
			// cout << tmp2 << endl;
			R.replace(i,k, tmp2);
			R.replace(j, k, tmp);
		}
		tmp = c * Q(k, j) + s * Q(k , i);
		tmp2 = - s * Q(k, j) + c * Q(k, i);
		Q.replace(k,i, tmp2);
		Q.replace(k, j, tmp);
	}
	return ;
}


void givens(MapMatrix<Cplx>& A, MapMatrix<Cplx>& Q, MapMatrix<Cplx>& R){
	for (int i =0; i<NbRow(Q); i++){
		Q.replace(i,i,Cplx(1.,0.));
	}
	// cout << Q << endl;
	// printf("building of Q\n");
	R = A;
	// memcpy(R,A,NbRow(A)*NbCol(A)*sizeof(Cplx));
	for (int j = 0; j<NbCol(A); j++){
		for (int i = j+1; i<NbRow(A); i++){
			// cout <<R << endl;
			givens_ij(R, Q, i, j);
		}
	}
	return ;
}


MapMatrix<Cplx> update_Q(MapMatrix<Cplx>& Q, MapMatrix<Cplx>& H, int k){
	cout <<"entréé update" << endl;
	int n = NbRow(Q);
	MapMatrix<Cplx> nQ (n+1, n+1);
	// cout <<n << endl;
	// cout  << nQ <<endl; 
	Cplx rjj = H(n-2, n-2);
	cout << "rjj: " << rjj << endl;
	Cplx rij = H(n-1, n-2);
	cout << "rij: " << rij << endl;
	Cplx x = sqrt(rjj*rjj+rij*rij);
	Cplx c = rjj/x;
	Cplx s = rij/x;
	Cplx tmp, tmp2;
	// cout <<"entréé update" << endl;
	// cout << "Q =" << Q << endl;
	for (int i = 0; i< n ; i++){
		for (int j = 0; j< n ; j++){
			nQ.replace(i,j,Q(i,j));
		}
	}
		
	for (int l = 0; l< n; l++) {
		tmp = c * Q(l, n-1) ;
		tmp2 =  s * Q(l, n-1) ;
		nQ.replace(l,n, tmp2);
		nQ.replace(l, n-1, tmp);
	}
	for (int i = 0; i< n ; i++){
		tmp =  s ;
		tmp2 = c ;
		nQ.replace(i, n, tmp);
	}
	tmp = -s;
	nQ.replace(n, n-1, tmp);
	nQ.replace(n, n, tmp2);
	// cout <<"sortie update" << endl;
	return nQ;
}
		
		
MapMatrix<Cplx> update_R(MapMatrix<Cplx>& R, MapMatrix<Cplx>& _Q, MapMatrix<Cplx>& H, int k){
	// cout <<"entréé update" << endl;
	int n = NbRow(R);
	int p = NbCol(R);
	vector<Cplx> v (n);
	MapMatrix<Cplx> nR (n+1, p+1);
	// cout <<n << endl;
	// cout  << nQ <<endl; 
	Cplx rjj = H(n-2, n-2);
	cout << "rjj: " << rjj << endl;
	Cplx rij = H(n-1, n-2);
	cout << "rij: " << rij << endl;
	Cplx x = sqrt(rjj*rjj+rij*rij);
	Cplx c = rjj/x;
	Cplx s = rij/x;
	Cplx tmp, tmp2;
	// cout <<"entréé update" << endl;
	// cout << "nrow qt " << NbRow(_Q) << "nrow r " << NbRow(R) << "nrow H" << NbRow(H) << endl;
	// cout << "nrow qt " << NbCol(_Q) << "nrow r " << NbCol(R) << "nrow H" << NbCol(H) << endl;
	for (int i = 0; i< n ; i++){
		Cplx a {};
		for (int j = i; j< n; j++){
			a += H(j,n-1) *_Q(i,j);
			if (j <p){
				nR.replace(i,j,R(i,j));
			}
		}
		v[i] = a;
	}
	// cout << "and..." << endl;
	for (int l = 0; l< n; l++) {
		nR.replace(l,n, v[l]);
	}
	// cout << "and..." << endl;
	tmp = s* R(n-1,p-1);
	tmp2 = c* R(n-1,p-1);
	nR.replace(n, p-1, tmp);
	nR.replace(n-1, p-1, tmp2);
	nR.replace(n-1, p, v[n-1]*c - s*rij);
	nR.replace(n, p, v[n-1]*s + c*rij);
	// cout <<"sortie update" << endl;
	return nR;
}
		
		
	
void Arnoldi (vector<vector<Cplx>>& vk, MapMatrix<Cplx>& A, MapMatrix<Cplx>& H, vector<Cplx>& v, int k, int K){
	//Assume that Arnoldi (0, ..., k-1) has been call previously
	int n = vk.size();
	// cout << "size" << n << endl; 
	vector<Cplx> _vj;
	if (n == 0){
		vk.push_back(v*(1/Norm(v)));  //v0
		n = n+1;
		// cout << vk << endl;
	}
	// cout << v << Norm(v) << endl;
	double N;
	// int j = k;
	for (int j = n-1; j< K; j++){
		for (int i = 0; i<= j; i++){
			H.insert(i,j,(vk[i],(A*vk[j])));
		}
	    // cout << (A*vk[0],v) << endl;	
		vector<Cplx> s(v.size()) ;
		for (int p = 0; p<=j; p++){
			s = s + vk[p]*H(j,p);
		}
		// cout << s.size() << (A*vk[j] ).size() << endl;
		_vj = A*vk[j] - s;
		N = Norm(_vj) ;
		H.insert(j+1,j,N);
		if ( is_nul(_vj) == false) {
			// cout << _vj << endl;
			if ( j != K-1){
				vk.push_back(_vj*(1/N));
			}
		}else{
			// cout << _vj << endl;
			cout << "breaaaaak !!" << endl;
			break;
			return ;
		}
	}
	return ;
}
 	
int GMResSolve(MapMatrix<Cplx>& A, vector<Cplx>& x, const vector<Cplx>& b, vector<Cplx>& y, int restart, double tol, int maxit, double& residual){
	cout << "start GMRES" << endl;
	vector<Cplx> r = b - A*x;
	cout << " r is computed" << endl;
	int k = 0;
	int n = x.size();
	double r_norm = Norm(r);
	double b_norm = Norm(b);
	double norm = r_norm/b_norm;
	MapMatrix<Cplx> _R(maxit, maxit+8);
	MapMatrix<Cplx> _Q(maxit, maxit+8);
	MapMatrix<Cplx> nQ(0,0);
	vector<Cplx> _g (maxit);
	vector <vector<Cplx>> vk;
	MapMatrix<Cplx> Q(1, 1);
	MapMatrix<Cplx> R(1, 1);
	 // Arnoldi (vk, A, H, r, k, k);
	 // MapMatrix<Cplx> Q(2,2);
	 cout << "erreur: " << norm << endl;
	while ( norm>tol && k < restart){
		k = k+1;
		cout << "iteration " << k << endl;
		MapMatrix<Cplx> H(k + 1, k);
	    Arnoldi (vk, A, H, r, k, k);
		// cout << "Arnoldi vector; " << vk << endl;
		// cout << "H = " << H << endl;
		// cout << "R = " << R << endl;
		
		
		if (k == 1){
			MapMatrix<Cplx> __Q(k + 1,k + 1);
			MapMatrix<Cplx> __R(k + 1,k );
			// cout <<  "Q = " << __Q << endl;
			givens(H, __Q, __R);
			// cout <<  "Q = " << __Q << endl;
			Q = __Q;
			R = __R;
			// cout <<  "Q = " << Q << endl;
			// cout << "R = " << R << endl;
		}else{
			// Q(k ,k );
			MapMatrix<Cplx> nQ = update_Q(Q, H, k);
			MapMatrix<Cplx> _Q = Q.herm();
			MapMatrix<Cplx> nR = update_R(R, _Q, H, k);
			// Q(k + 1,k + 1);
			// MapMatrix<Cplx> __Q(k + 1,k + 1);
			// givens(H, __Q, R);
			// Q = __Q;
			// cout <<  "Q = " << Q << endl;
			// cout <<  "nQ = " << nQ << endl;
			// cout <<  "nR = " << nR << endl;
			// cout << "Q = " << Q << endl;
			Q = nQ;
			R = nR;
		}
		MapMatrix<Cplx> _Q = Q.herm();
		MapMatrix<Cplx> F = Q*R;
		// cout << "H?" << F << endl;
		vector<Cplx> g (k);
		for (int i = 0; i< k; i++){
			g[i] = r_norm * _Q(i,0);
		}
		// cout << "herm done "  << _Q  << endl;
		Cplx gamma = r_norm * _Q(k,0); 
		// cout << "g = " << g << endl;
		cout << "gamma = " << gamma << endl;
		// r_norm = abs(gamma);
		r_norm = abs(gamma);
	    norm = r_norm/b_norm;
		_R = R;
		_Q = Q;
		_g = g;
		cout << "erreur: " << norm << endl;
	}
	
			
	cout << "sortie du while" << endl;
	// cout << "we solve Rt = g with R = " << _R << endl;
	// cout << "and t = " << _g << endl; 	
	// cout << "t = " << t << endl;
	vector<Cplx> t = _R.Solve_R(_g);
	vector<Cplx> _x(n);
	// cout << "solve: " << t << endl;
	// cout << "final vk: " << vk << endl;
	// Vk * t
	for (int i = 0; i< n; i++){
		Cplx a {};
		for (int j = 0; j< k; j++){
			a += t[j]*(vk[j])[i];
		}
		_x[i] = a;
	}
	cout << "nb of iteration: " << k << endl;
	cout << "erreur final: " << norm << endl;
	// cout << "the solution is " << _x + x << endl;
	// cout << "the guess was " << x << endl;
	cout << endl << endl << "verification: " << endl;
	// cout << "ce que j'ai computed: " << A* (_x + x) << "ce que a devrait être: " << b << endl;
	y =  _x + x;
	residual = Norm(r - _x);
	if (norm<tol){
		return 1;
	}else{
		return 0;
	}
}

vector<Cplx> GMResSolve_restart(MapMatrix<Cplx>& A, vector<Cplx>& x, const vector<Cplx>& b, int restart, double tol, int maxit, const string& filename){
	ofstream file(filename);
	file << "x" << " " << "y"<< endl;
	double residual;
	int k = 0;
	int end = 0;
	vector<Cplx> y(NbRow(A));
	while (k < maxit){
		if (end ==0){
			// cout << "NEW GUESS: " << x << endl;
		    end = GMResSolve(A, x, b, y, restart, tol, end, residual);
			x = y;
			k++;
			cout << "number of gmres: " << k << endl;
			file << k << " " << residual << endl;
		}else{
			break;
		}
	}
	return y;
}
		
		
		
		
		

#endif