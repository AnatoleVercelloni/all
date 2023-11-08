#include<stdlib.h>
#include<stdio.h>
#include<time.h>
#include<string.h>

int TAB[10] = {10,20,50,100,500,1000,2000,5000,10000,50000};

void ShowArray(int *A, int N){
	printf("A = ");
	for (int i = 0; i<N; i++){
		printf("%d  ",A[i]);
	}
	printf("\n");
}
void RandArray(int *A, int N){
	for (int j = 0; j<N; j++){
			A[j] = rand();
		}
}

void BubbleSort(int *A, int N){
	for (int i = 0; i<N; i++){
		for (int j = 0; j<N-i-1; j++){
			if (A[j]>A[j+1]){
				int tmp = A[j];
				A[j] = A[j+1];
				A[j+1] = tmp; 
			}
		}
	}
}


void InsertionSort(int *A, int N){
	for (int i = 1; i<N; i++){
		for (int j = i; j>0 && A[j]<A[j-1]; j--){
				int tmp = A[j];
				A[j] = A[j-1];
				A[j-1] = tmp;
		}
	}
}

void Merge(int *A, int p, int q, int r){
	int *S = malloc((r-p+1)*sizeof(int));
	int u = 0;
	int v = q - p +1 ;
	int n = r-p+1;
	for (int i = 0; i<n; i++){
		S[i] = A[i+p];
	}
	for (int j = p; j<=r; j++){
		if ((u<=q-p && S[u]<=S[v]) || v>=n){
			A[j] = S[u];
			u = u + 1;		
		}else{
			A[j] = S[v];
			v = v + 1;	
		}
	//printf("%d, %d, %d, %d\n", j, u, v, A[j]);
	}
	free(S);
}
	
void MergeSort(int *T, int p, int r){
	if(p<r){
		int q = (p+r)/2;
		MergeSort(T,p,q);
		MergeSort(T,q+1,r);
		// printf("Merge(%d,%d,%d)\n",p,q,r);
		Merge(T,p,q,r);
	}
}

void Merge2(int *A, int *S, int p, int q, int r){
	int u = p;
	int v = q + 1;
	for (int i = p; i<=r; i++){
		S[i] = A[i];
	}
	for (int j = p; j<=r; j++){
		if ((u<=q && S[u]<=S[v]) || v>=r+1){
			// printf("yess ");
			A[j] = S[u];
			u = u + 1;		
		}else{
			A[j] = S[v];
			v = v + 1;	
		}
		// printf("ind : %d, %d, %d, %d\n", j, u, v, A[j]);
	}
}
	

void MergeSort2(int *A, int N){
	int *S = malloc(N*sizeof(int));
	for (int i = 0; i<N; i++){
		S[i] = A[i];
	}
	// memcpy(S,A,N*sizeof(int));
	int p = 0;
	int pas = 1;
	int n = N;
	while(n>2){
		n = (n+1)/2;	//n = nombre de tableaux
		pas = pas*2;
		for (int i = 0; i<n; i++){
			p = i*pas;
			if (i==n-1){
				if (p != N-1){ 
					// printf("%d,%d,%d",p,(p + N - 1)/2,N-1);
					Merge2(A, S, p,(p + N - 1)/2,N-1);
					
				}
			}else{
				// printf("%d,%d,%d    ",p,p + (pas - 1)/2,p + pas - 1);
				Merge2(A, S, p,p + (pas - 1)/2,p + pas - 1);
			}
		}
		//printf("\n");
	}
	// ShowArray(A,N);
	// printf("%d\n",p);
	Merge2(A, S, 0,p-1, N-1);
	// ShowArray(A,N);
	free(S);
}


int main(){
	srand(time(NULL));
	FILE *f = fopen("timeCPU.txt", "w");
	
	clock_t temps_initial, temps_final;  
	double temps_cpu;  


	for (int i =0; i<10; i++){
		int N = TAB[i];
		fprintf(f, "%d ", N);
		int* A = malloc(N*sizeof(int));
		RandArray(A, N);

		temps_initial = clock();
		BubbleSort(A,N);
		temps_final = clock ();

		fprintf(f, "%f ", (double) (temps_final - temps_initial) / CLOCKS_PER_SEC*1000);
		RandArray(A, N);

		temps_initial = clock();
		InsertionSort(A,N);
		temps_final = clock ();

		fprintf(f, "%f ",  (double)(temps_final - temps_initial) / CLOCKS_PER_SEC*1000);
		RandArray(A, N);

		temps_initial = clock();
		MergeSort(A,0,N-1);
		temps_final = clock ();
		
		fprintf(f, "%f ",  (double)(temps_final - temps_initial) / CLOCKS_PER_SEC*1000);
		RandArray(A, N);

		temps_initial = clock();
		MergeSort2(A,N);
		temps_final = clock ();

		fprintf(f, "%f ", (double) (temps_final - temps_initial) / CLOCKS_PER_SEC*1000);

		free(A);
		fprintf(f,"\n");
	}
	// int A[11] = {5,32,98,51,22,12,44,3,6};
	// ShowArray(A,9);
	
	// MergeSort2(A,9);
	return 0;
}


		
