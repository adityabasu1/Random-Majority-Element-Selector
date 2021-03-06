# Random-Majority-Element-Selector

Python code to implement a Random Majority Element Selector and verify convergence of average number of iterations<br />
   
## **Running The Code** <br />
Command: ```python3 code.py``` <br />
Recommended ```NUMBER OF SIMULATIONS```: 10000 (should be atleast 2000) (the more the merrier) <br />
Approximate run-time for 1E6 simulations: 3.82 seconds <br />

## Input <br />
- An array ```A``` containing a majority element <br />
- NOTE: If no input is given, a sample array (hard-coded) will be taken <br />

## Definitions <br />
For an array ```A``` containing a majority element ```maj```: <br />
- ```n```: total number of elements in A <br />
- ```m```: number of occurences of the maj in A <br />

## What is a Majority Element? <br />
- Let ```A``` be an array with ```n``` elements<br />
- An element maj is called a majority element in A if ```maj occurs MORE THAN n / 2``` times in A<br />
- Every array need not contain a majority element. But if it does, the majority element is unique <br />
- ``` NOTE: FOR OUR CASE, THE EXISTENCE OF A MAJORITY ELEMENT IS COMPULSORY ```  <br />
- Examples: 
  - [1,2,2,2] -> majority element = 2
  - [1,5,5,5,4,5,4] -> majority element = 5 <br />
- Non-examples: 
  - [1,2,1,2], [1,2,3,4] -> do not have a majority element <br />
   
## Algorithm <br />
Given the array A with a majority element: <br />
- We ```randomly pick an element```<br />
- Check if it is the majority element. <br />
  - If it is, we return it. <br />
  - If it isn't, we ```repeat``` the process till we find the majority element. <br />
 
This is an example of a ```Monte Carlo``` Algorithm:
- ```Non-deterministic output```
- ```Deterministic runtime```

## Mathematical Insight <br />
- (# iterations) is a geometric random variable with ```p = m/n``` [Since we iterate till we get the majority element] <br />
- The results we get are in accordance with the Law of Large Numbers 
i.e with very high number of simulations, the average number of iterations converges to its expected value ```n/m``` <br />
- We also verify the following using a ```plot```<br />

## Example Generated Plot:
![RMES2](https://user-images.githubusercontent.com/60356270/177551544-4f7f14a1-0975-4fe3-b8c9-c7ee0ba5a5af.jpeg)
   
## Useful Links <br />
Related intersting problems on Majority Element: https://cse.iitkgp.ac.in/~abhij/course/lab/Algo1/Autumn14/A8.pdf <br />







   
