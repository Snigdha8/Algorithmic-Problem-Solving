### Homework 2

Q1. Use bit tricks/techniques to solve these problems. <br>
(i) [5 points] Given an unsigned integer x, determine if it is a multiple of 8. Show the working of your logic using a 16-bit example. <br>
<b>Answer:</b>

```java
import java.io.*;

class BitTricks {
	public static void main (String[] args) {
		int[] x = {24, 23, 8580, 10128, 33256};
		
		System.out.println("Check by anding");
		for(int i=0;i<x.length;i++) {
		    System.out.println(checkDivisibilityByEightByAnding(x[i]));
		}
        
        System.out.println("Check by shifting");
        for(int i=0;i<x.length;i++) {
		    System.out.println(checkDivisibilityByEightByAnding(x[i]));
		}		
	}
	
	private static boolean checkDivisibilityByEightByAnding(int x) {
	    // The lower 3 bits of x must be 0 if x is divisible by 8
	    if((x & 7) == 0) {
		    return true;
		}
		else {
		    return false;
		}
	}
	
	private static boolean checkDivisibilityByEightByShiftingBits(int x) {
	    // Drop the last 3 digits of the number by right shifting
	    int temp = x >> 3;
	    // Then, left shift the temp by 3 shifts
	    temp = temp << 3;
	    
	    // If temp matches x then, x is divisible by 8
	    if(temp == x) {
	        return true;
	    }
	    else {
	        return false;
	    }
	}
}
```

Q6. Consider the multiset [3,3,3,3,3,2,2,2,1,1,1,4,4,4,4,4,4,4] <br>
We will construct a count-min sketch (CMS) to store the counts of these numbers. We will use w = 12 and k = 3. <br>
The hash seeds for the three hash functions are 14, 3, 10 in the same order. <br>
Below is the code used to hash the numbers into the buckets: <br>
```
Hash(num, seed):
  hash = num x 31
  hash = hash + seed
  hash = hash mod w
  return hash
```
a) [5 points] Show the state of the filter (the value of the buckets) after we insert all the 3s, then all the 2s, then all the 1s, then all the 4s. <br>
b) [5 points] Query the CMS for the count of the numbers 1,2,3,4 and 5 and show the results of each query. <br>
c) [5 points] Now suppose we insert the value 16 into our CMS. Show the state of the CMS after this insert. <br>
d) [5 points] Now we query the filter for the value 4 again. What does the query return? <br>

<b>Answer:</b><br>
```
Q6 a. Show the state of the filter
Initial matrix
0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 

State of the filter after inserting all 3s
0 0 0 0 0 0 0 0 0 0 0 5 
5 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 5 0 0 0 0 

State of the filter after inserting all 2s
0 0 0 0 3 0 0 0 0 0 0 5 
5 0 0 0 0 3 0 0 0 0 0 0 
3 0 0 0 0 0 0 5 0 0 0 0 

State of the filter after inserting all 1s
0 0 0 0 3 0 0 0 0 3 0 5 
5 0 0 0 0 3 0 0 0 0 3 0 
3 0 0 0 0 3 0 5 0 0 0 0 

State of the filter after inserting all 4s
0 0 0 0 3 0 7 0 0 3 0 5 
5 0 0 0 0 3 0 7 0 0 3 0 
3 0 7 0 0 3 0 5 0 0 0 0 

Q6 b. Query the CMS for the count of the numbers 1,2,3,4 and 5
Query count of 1 = 3
Query count of 2 = 3
Query count of 3 = 5
Query count of 4 = 7
Query count of 5 = 0

Q6 c. Insert 16
State of the filter after inserting 16
0 0 0 0 3 0 8 0 0 3 0 5 
5 0 0 0 0 3 0 8 0 0 3 0 
3 0 8 0 0 3 0 5 0 0 0 0 

Q6 d. Query for 4
Query count of 4 = 8
```
Below is the Java code: 
```java
import java.io.*;

public class CountMinSketch {
    private static int k;
    private static int w;
    private static int seed[] = {14, 3, 10};
    private static int A[][];

    CountMinSketch(int k, int w) {
        this.k = k;
        this.w = w;
    }

    public static void main(String[] args) {
        int numHashFunctions = 3;
        int width = 12;
        A = new int[numHashFunctions][width];
        int[] x = {3,3,3,3,3,2,2,2,1,1,1,4,4,4,4,4,4,4};
        
        CountMinSketch countMinSketch = new CountMinSketch(numHashFunctions, width);

        // Q6 a. Show the state of the filter
        System.out.println("Q6 a. Show the state of the filter");
        System.out.println("Initial matrix");
        printA();
        System.out.println();

        update(3, 5);
        System.out.println("State of the filter after inserting all 3s");
        printA();
        System.out.println();

        update(2, 3);
        System.out.println("State of the filter after inserting all 2s");
        printA();
        System.out.println();

        update(1, 3);
        System.out.println("State of the filter after inserting all 1s");
        printA();
        System.out.println();

        update(4, 7);
        System.out.println("State of the filter after inserting all 4s");
        printA();
        System.out.println();


        // Q6 b. Query the CMS for the count of the numbers 1,2,3,4 and 5 
        System.out.println("Q6 b. Query the CMS for the count of the numbers 1,2,3,4 and 5");
        System.out.println("Query count of 1 = " + estimate(1));
        System.out.println("Query count of 2 = " + estimate(2));
        System.out.println("Query count of 3 = " + estimate(3));
        System.out.println("Query count of 4 = " + estimate(4));
        System.out.println("Query count of 5 = " + estimate(5));
        System.out.println();

        // Q6 c. Insert 16
        System.out.println("Q6 c. Insert 16");
        update(16, 1);
        System.out.println("State of the filter after inserting 16");
        printA();
        System.out.println();

        // Q6 d. Query for 4
        System.out.println("Q6 d. Query for 4");
        System.out.println("Query count of 4 = " + estimate(4));
    }

    private static void update(int x, int countX) {
        int i;
        for (i = 0; i < k; i++) {
            A[i][Hash(x, seed[i])] += countX;
        }
    }

    private static int estimate(int x) {
        int minCount = A[0][Hash(x, seed[0])];

        for (int i = 1; i < k; i++) {
            int column = Hash(x, seed[i]);
            if (A[i][column] < minCount) {
                minCount = A[i][column];
            }
        }

        return minCount;
    }

    private static int Hash(int num, int seed) {
        int hash = num * 31;
        hash = hash + seed;
        hash = hash % w;
        return hash;
    }

    private static void printA() {
        int i, j;
        for (i = 0; i < k; i++) {
            for (j = 0; j < w; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```


