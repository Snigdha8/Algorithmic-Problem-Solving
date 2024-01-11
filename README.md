During my **Master's in Computer Science** from **Stony Brook University**, I studied the course - **Algorithmic Problem Solving.** <br>
In this repository, you will come across some amazing algorithms that are very useful and have wide applications. <br>
You can see the list of algorithms covered below. You will find the code to the below algorithms in the below serial number. (file name may be different, but serial number matches with those in the file names) <br>
1. **Brute Force PageRank Algorithm:** <br>
   This algorithms converges after some iterations and finally we can rank the pages based on their page rank values.
2. **Page Rank using Eigenvectors**
3. **Brute Force PageRank with teleportation factor:** <br>
   This algorithm converges in fewer iterations compared to the brute force algorithm.
4. **Page Rank using Eigenvectors with teleportation factor**
5. Python code to plot the pagerank values of the pages (in a single plot) in the digraph as a function of the teleportation factor (varying the factor like this: 0.1, 0.2, 0.3, so on till 0.9)
6. **Page Rank using repeated squaring method without teleportation factor**
7. Find **all matching occurrences** of a **pattern** within the **larger text string** using **Rabin Karp Algorithm**.<br>
   The actual was as follows:<br>
    	Consider the text string “mississippippissi”. We wish to find all matching occurrences of the
	pattern “ippi” within the larger text string. Assume that Σ = {a, b, c, … , z}.
	(i) [10 points] Apply Rabin-Karp. Show the value of the rolling hash in each step. Also show the
	value of the hash for the pattern “issip”. When calculating the hashes of the strings, characters
	should be converted to integers by calculating their offset from the character ‘a’. That is, the
	letter ‘c’ would have a value of ‘c’-’a’ = 2 and the character ‘z’ would have a value of 25. When
	calculating the polynomial hash, set the base of the polynomial to be 13, and the hash modulus
	to be 31.<br>
   The output was as below: <br>
   	Pattern is “ippi” Pattern Hash is 9 <br>
	miss : 6 <br>
	issi : 28 <br>
	ssis : 23 <br>
	siss : 13<br>
	issi : 28<br>
	ssip : 20<br>
	sipp : 2<br>
	ippi : 9<br>
	Pattern found starting at index : 7<br>
	ppip : 21<br>
	pipp : 14<br>
	ippi : 9<br>
	Pattern found starting at index : 10<br>
	ppis : 24<br>
	piss : 25<br>
	issi : 28<br>
	Pattern is “issip” Pattern Hash is 7
