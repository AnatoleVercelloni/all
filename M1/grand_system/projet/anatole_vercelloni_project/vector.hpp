#ifndef VECTOR_HPP
#define VECTOR_HPP
#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <complex>

using namespace std;
typedef complex<double> Cplx;

template<typename T>
void operator+=(vector<Cplx> &v1, vector<T> &v2){
	assert(v1.size() == v2.size());
	for (int i = 0; i<v1.size(); i++){
		v1[i] = v1[i] + v2[i];
	}
}

template<typename T>
void operator-=(vector<Cplx> &v1, vector<T> &v2){
	assert(v1.size() == v2.size());
	for (int i = 0; i<v1.size(); i++){
		v1[i] = v1[i] - v2[i];
	}
}

template<typename T>
vector<Cplx> operator+(const vector<Cplx> &v1, const vector<T> &v2){
	vector<Cplx> v3;
	assert(v1.size() == v2.size());
	for (int i = 0; i<v1.size(); i++){
		v3.push_back(v1[i] + v2[i]);
	}
	return v3;
}

template<typename T>
vector<Cplx> operator-(const vector<Cplx> &v1, const vector<T> &v2){
	vector<Cplx> v3;
	assert(v1.size() == v2.size());
	for (int i = 0; i<v1.size(); i++){
		v3.push_back(v1[i] - v2[i]);
	}
	return v3;
}


template<typename T>
Cplx operator,(const vector<T> &v1, const vector<T> &v2){
	T a {};
	assert(v1.size() == v2.size());
	for (int i = 0; i<v1.size(); i++){
		a+=conj(v1[i])*v2[i];
	}
	return a;
}

template<typename T>
double Norm(const vector<T> &v){
	double n = 0.0;
	for(int i = 0; i<v.size(); ++i){
		n += v[i]*v[i];
	}
	return sqrt(n);
}

template<>
double Norm<Cplx>(const vector<Cplx> &v){
	double n = 0.0;
	for(int i = 0; i<v.size(); ++i){
		n += real(conj(v[i])*v[i]);
	}
	return sqrt(n);
}


template<typename T>
void operator*=(vector<Cplx> &v, T a){
		for (int i = 0; i<v.size(); i++){
			v[i] = a*v[i];
		}
}

template<typename T>
vector<Cplx> operator*(const vector<Cplx> &v, const T a){
	vector<Cplx> v2;
	for (int i = 0; i<v.size(); i++){
			v2.push_back(a*v[i]);
		}
	return v2;
}



template<typename T>
ostream &operator<<(ostream &o, const vector<T> &v){
	for (const auto& uj:v){ o << uj << "\t";}
	return o << endl;
}

template<>
inline ostream &operator<<<Cplx>(ostream &o, const vector<Cplx> &v){
	for (const auto& uj:v){
		if (uj.imag()>0){
			o << uj.real() << "+" << uj.imag() << "i" << "\t";
		}else{
			if (uj.imag()<0){
			o << uj.real() << "" << uj.imag() << "i" << "\t";
			}else{
				o << uj.real() << "\t";
			}
		}
	}
	return o << endl;
}


template<typename T>
bool is_nul (vector<T> v){
	T zero {};
	for (int i = 0; i< v.size(); i++){
		if (v[i] != zero){
			return false;
		}
	}
	return true;
}


vector<Cplx> LoadVector(const string& filename, int size){
		ifstream file(filename);
		if (file){
			double real;
			double imag;
			int i = 0;
			vector<Cplx> u(size);
			string line;
			while (file >> real) {
				file >> imag;
				Cplx v(real, imag);
				u[i] = v;
				// cout << i << endl;
				i++;
			}
			return u;
				
		}else{
			cout << "file opening error\n";
			exit(1);
		}
	}


#endif