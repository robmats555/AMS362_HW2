#include <iostream>
#include <random>
#include <chrono>
#include <fstream>
  
using namespace std; 
  
#define S 1024
#define L 4096

// This function multiplies  
// mat1[][] and mat2[][], and  
// stores the result in res[][] 
void multiply_small(double mat1[S][S],  
              double mat2[S][S],  
              double res[S][S]) 
{ 
    int i, j, k; 
    for (i = 0; i < S; i++) 
    { 
        for (j = 0; j < S; j++) 
        { 
            res[i][j] = 0; 
            for (k = 0; k < S; k++) 
                res[i][j] += mat1[i][k] *  
                             mat2[k][j]; 
        } 
    } 
}

void multiply_large(double mat1[L][L],  
              double mat2[L][L],  
              double res[L][L]) 
{ 
    int i, j, k; 
    for (i = 0; i < L; i++) 
    { 
        for (j = 0; j < L; j++) 
        { 
            res[i][j] = 0; 
            for (k = 0; k < L; k++) 
                res[i][j] += mat1[i][k] *  
                             mat2[k][j]; 
        } 
    } 
}

// Driver Code 
int main() 
{ 
    int i, j; 

    static double small_result[S][S]; // To store 1024 x 1024 result 
    static double large_result[L][L]; // To store 4096 x 4096 result 

    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator (seed);
    std::uniform_real_distribution<double> distribution(-1.0,1.0);

    static double a[S][S];
    static double b[S][S];

    static double x[L][L];
    static double y[L][L];


    for( i = 0; i < S; ++i){
        for( j = 0;  j < S; ++j){
            a[i][j] = distribution(generator);
            b[i][j] = distribution(generator);
        }
    }
    for( i = 0; i < L; ++i){
        for( j = 0;  j < L; ++j){
            x[i][j] = distribution(generator);
            y[i][j] = distribution(generator);            
        }
    }
  
    multiply_small(a, b, small_result); 
    
    std::ofstream out10("naive-10.csv");
    for (auto& row : small_result) {
        for (auto col : row)
            out10 << col <<',';
            out10 << '\n';
    }

    multiply_large(x, y, large_result); 
    
    std::ofstream out12("naive-12.csv");
    for (auto& row : large_result) {
        for (auto col : row)
            out12 << col <<',';
            out12 << '\n';
    }

    return 0;
} 
  