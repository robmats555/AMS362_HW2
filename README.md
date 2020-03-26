# Problem #1

## Setup
In the first problem, we are asked to implement the naive and Strassen method of multiplication for two matrices whose contents are random numbers generated from a uniform distribution and range from (-1,1).


## Algorithm Description: Naive Method
The naive method requires a nested nested for loop. If the two matrices are X and Y, the algorithm iterates through the rows of X, then the columns of Y, and then the rows of Y. This simulates how one row of X multiples a column of Y and so forth to do the multiplication. 

## Algorithm Description: Strassen Method
A recursive algorithm is used for Strassen. As professor Deng said we can stop the algorithm after at least three levels so I use the built in numpy matrix multiplier once the dimensions of the inputted matrix are 2^7 x 2^7 as a base case. Otherwise, I split the matrix into four pieces and then apply the additions and subtractions to it as shown below. 

<img src="strassen_algo.PNG" width=500>

The final pieces (The C__) are reassembled into on matrix which is the result.

## Pseudocode (Naive):
    def matrix_multiply(X, Y):
        result = generate_result_matrix(len(X))
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        return result

## Pseudocode (Strassen):
    def matrix_multiply(A, B):
        if the matrix has a shape of 2^7 x 2^7 use built-in Python methods to multiply:
            return multiplication of A and B by numpy
        else:
            Create the four pieces of the first input matrix
            Create the four pieces of the second input matrix
            Carry out the 7 multiplications and store them
            Add up the multiplications into the four quarters of the result
            Reassemble the result matrix and return it

## Answer
A comparison of the matmul 

Naive Additions: (2^10 - 1) * (2^10 * 2^10) <br/>
Naive Multiplications: 2^10 * 2^10 * 2^10 <br/>

Note 1: This assumes that np.matmul uses a naive approach <br/>
Note 2: na(x) and nm(x) represent the number of additions and multiplications given x rows and columns <br/>
Strassen Additions: <br/>
786895335   - 2294154 + na(x) for 2^10 x 2^10 <br/>
38557871487 - 2294154 + na(x) for 2^12 x 2^12 <br/>
This comes from the recurrence relation f(t) = 7 * f(t-1) + 9 where f(0) = 18 <br/>
This is because there are 7 times the Strassen mutliplication would be called recursively and then the 9 additions that are conducted when the 'M' pieces are turned into the 'C' pieces. The base case is 18 because in the 2 x 2 case there are just 18 additions. 786895335 is <br/>

