The requirements to run the Strassen.py file are numpy and pandas.
The requirements to compile the Naive.cpp file are a compiler for C++ and iostream, random, chrono, and fstream (Those should already be there, but just for thoroughness). 
The requirements to run the CoronaCases.py program are matplotlib, numpy, random, and math libraries.

# Problem #1

## Setup
In the first problem, we are asked to implement the naive and Strassen method of multiplication for two matrices whose contents are random numbers generated from a uniform distribution and range from (-1,1).


## Algorithm Description: Naive Method
The naive method requires a nested nested for loop. If the two matrices are X and Y, the algorithm iterates through the rows of X, then the columns of Y, and then the rows of Y. This simulates how one row of X multiples a column of Y and so forth to do the multiplication. The algorithm then deposits the result in a csv (naive-10 for 2^10 x 2^10 multiplication and naive-12) that is in the same directory. (I did this one in C++ because the Python version takes significantly longer and the 2^12 x 2^12 takes a very long time still.) 

## Algorithm Description: Strassen Method
A recursive algorithm is used for Strassen. As professor Deng said we can stop the algorithm after at least three levels so I use the built in numpy matrix multiplier once the dimensions of the inputted matrix are 2^7 x 2^7 as a base case. Otherwise, I split the matrix into four pieces and then apply the additions and subtractions to it as shown below. I then put the results in a csv (strassen-10 and strassen-12). I also put the default numpy multiplication results in csvs (default-10 and default-12) as a comparison. 

<img src="strassen_algo.PNG" width=500>

The final four quarters, the C__ , are reassembled into the matrix, which is the result.

## Pseudocode (Naive):
    def matrix_multiply(X, Y):
        result = generate_result_matrix(len(X))
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] += X[i][k] * Y[k][j]
        return result
    send result to csv

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
    send result to csv

## Answer
Naive Additions: (2^10 - 1) * (2^10 * 2^10) <br/>
Naive Multiplications: 2^10 * 2^10 * 2^10 <br/>

Strassen Additions: <br/>
786895335   - 2294154 + numa(x)** for 2^10 x 2^10 <br/>
38557871487 - 2294154 + numa(x)** for 2^12 x 2^12 <br/><br/>

This comes from the recurrence relation f(t) = 7 * f(t-1) + 9 where f(0) = 18.
This is because there are 7 times the Strassen mutliplication would be called recursively and then the 9 additions that are conducted when the 'M' pieces are turned into the 'C' quarters. The base case is 18 because in the 2 x 2 case there are just 18 additions (I count subtraction as an addition of a negative number). 786895335 comes from how much we would have done if the algorithm written was totally recurisive and 2294154 was what wasn't done due to going to the default multiplication after 3 to 5 levels of recursion. The numa(x)** comes from how many additions were done by numpy. <br/>

Strassen Multiplications: <br/>
7^10 - 7^8 + numm(x)** for 2^10 x 2^10 <br/>
7^12 - 7^8 + numm(x)** for 2^12 x 2^12 <br/><br/>

On a 2x2 matrix there are 7 multiplications done and then each recursive call requires 7, so it is exponential in the number of multiplications required. Similar to the explanation for addition, we remove from the total the recursive calls we didn't do and add back in how many multiplications it takes for numpy to do the rest.
<br/><br/>


** numa(x) and numm(x) represent the number of additions and multiplications given x rows and x columns done by numpy <br/>

# Problem #2

## Setup
In the second problem we are tasked with plotting daily case numbers of coronavirus over a 90 day period where the percentage of new cases is determined by a normal random variable, whose mean and standard deviation were previously provided. 

## Algorithm Description (Point Generation):
Points were created using the Box-Muller method to turn uniformly distributed points into normally distributed points. Then another uniform distribution (0,1] was used to determine which of the two points was returned by the generating function. If the number fell below 0.5 then the number produced by the cosine version was used, otherwise the sine version was used. 

## Pseudocode (Point Generation):
    def point_generator(mean,standard_deviation):
        u1,u2 = generate two uniform random variables
        g1,g2 = apply box muller transform on them
        z1,z2 = multiply g1 and g2 by standard deviation and add mean
        
        if new uniform random variable (0,1] < 0.5:
            return z1
        else 
            return z2

## Algorithm Description (Interpolation):
I used points 1, 9, 18, 27, 36, and 45 because I wanted the curve to fit better than if 1 wasn't included. I then used the method of solving the system of equations, as shown in the image below, in order to find the coefficients of the function. 

<img src="interpolation_method.PNG" width=500>

## Pseudocode (Interpolation):
    def generate_interpolation_points(cases):
        X = create matrix of terms raised to increasing powers
        y = vector of case values
        a = solve Xa = y using numpy
        plot interpolation curve using t (1 to 90) and 'a' coefficients

## Algorithm Description (Curve Fitting):
In order to find an exponential fit, the log of the dependent variable was taken. Then the minimum of the least squares was found to get the coefficients a and b for what would be a linear set of points. Then exp(a) was taken in order to convert the coefficent back for the resultant exponential curve. This process is shown in the image below that was taken from Wolfram.

<img src="fitting_method.PNG" width=700>
## Pseudocode (Curve Fitting):
    def generate_fit(cases):
        t = a range of 45 to 90
        y = cases
        a, b = Use equations from image above to generate coefficients
        a = exp(a)
        plot(ae^bt)
        
## Answer:
The graph is shown in the image below. Obviously, the fitting could've been better, but the interpolation was certainly satisfactorily.

<img src="corona_cases_plot.png" width=500>


