"""
    Python code to implement a Random Majority Element Selector and verify convergence in average number of iterations
    Creator: Aditya Basu
    Run the code with: python3 code.py 
    Recommended NUMBER OF SIMULATIONS: 10000 (should be atleast 2000) (the more the merrier)
    Approximate run-time for 1E6 simulations: 3.82 seconds
    
    Input: (NOTE: If no input is given, a sample array(hard-coded) will be taken)
    An array "A" containing a majority element
    
    Context on Majority element:
    Let A be an array with n elements. An element maj is called a majority element in A if a occurs MORE THAN n / 2 times in the
    array A. Every array need not contain a majority element. But if it does, the majority element is unique.
    NOTE: FOR OUR CASE, THE EXISTENCE OF A MAJORITY ELEMENT IS COMPULSORY
    
        Examples: [1,2,2,2] -> majority element = 2; [1,5,5,5,4,5,4] -> majority element = 5
        Non-examples: [1,2,1,2], [1,2,3,4] -> do not have a majority element
    
    About the Algorithm:
    
    Given the array A with a majority element:
    1. We *randomly pick an element*
    2. Check if it is the majority element.
    3. If it is, we return it.
    4. If it isn't, we repeat the process till we find the majority element.

    Definitions:
    For an array A containing a majority element "maj":
    n = total number of elements in A
    m = number of occurences of the majority element in A
    
    Mathematical insight:
    1. (# iterations) is a geometric random variable with p = m/n
        [Since we iterate till we get the majority element]
        The results we get are in accordance with the Law of Large Numbers 
        i.e with very high number of simulations, the number of iterations converges to its expected value = 1/p = n/m
        We also verify the following using a plot
    
    2. Proof of correctness:
       failing is described as being not able to find the majority element in a particular iteration
       probability of failing [pr(fail)] = (1 - m/n)
       
       If we iterate N times,
       pr(fail) = (1 - m/n)^N 
       now m > n/2,
       thus, pr(fail) <= (1/2)^N
       
       thus we growing N, the probability of failing all times keeps on decreasing
       N = log(n), pr(fail) <= 1/n
       N = nlog(n), pr(fail) <= (1/n)^n
       
       This proves that after a decent number of iterations, we are guaranteed to get the majority element \
                                                                    with an extremely high probability
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def is_majority(A: np.ndarray, x: int):
    """
        Function to checks if x is the majority element in array A
        Returns: a boolean 
    """
    min_count_to_be_maj = len(A) // 2
    x_count = sum([(elem == x) for elem in A])
    return x_count >= min_count_to_be_maj


def get_majority_elem(A: np.ndarray):
    """ 
        Function to run a Monte carlo algorithm to get the majority element
        Monte Carlo algorithm: A randomized algorithm which non-deterministic output but deterministic runtime 
        So, essentially we run the algorithm several times before we get an accurate result
        (# iterations) is a geometric random variable
        
        Returns: a tuple - (majority element, number of iterations needed to find it)
    """
    ch = np.random.randint(len(A)) #random index chosen
    iters_till_maj = 1  # tracks the number of iterations of the loop till we get the majority element
    while not is_majority(A,A[ch]): #till we don't get majority element, we do this
        iters_till_maj += 1
        ch = np.random.randint(len(A)) #choose random index again
    return (A[ch],iters_till_maj) #return the majority element and the iterations needed to find it


def simulate(A: np.ndarray, num_sims: int = 10000): #default number of simulations = 1E4
    """ 
        Re-performing the experiment several times to prove convergence 
        of average number of iterations needed to find the majority element
        (LAW OF LARGE NUMBERS)
        
        Returns: a dictionary containing the {number of simulations: average number of iterations \
                                                                needed to get majority element}
    """
    avg_itrs = dict()
    total_itrs_yet = 0
    for i in range(num_sims):
        maj_elem,itr_count = get_majority_elem(A)
        total_itrs_yet += itr_count #itr_count is the number of iterations needed to get majority element
        avg_itrs[i+1] = avg_itrs.get(i+1,total_itrs_yet/(i+1))
    return avg_itrs

def visualize(d: dict, m, n):
    """ 
        d: a dictionary
        key: number of simulatons
        values: average number of iterations needed to get majority element
        
        Function to visualize convergence of average number of iterations needed to get majority element \
                                             using the Monte Carlo algortihm
    """

    itr_nums = list(d.keys())
    itr_vals = list(d.values())

    plt.figure(figsize=(32,9))
    plt.title("Convergence")
    plt.xlabel("Number of simulations")
    plt.ylabel("Average number of iterations needed to get majority element")
    plt.plot(itr_nums, itr_vals)
    plt.axhline(y=n/m, color='r', linestyle="dotted")
    plt.show()

if __name__ == "__main__":
    
    choose_to_enter_data = bool(int(input("Do you want to enter data? Enter 1(Yes) or 0(No)\n")))
    
    
    A = [int(val) for val in input("Enter the list of values: ").rstrip().split(" ")] if choose_to_enter_data \
                                                        else [1,5,1,1,5,5,5,7,8,2,5,5,5]
    #A is the array entry that'll be passed for simulations
    
    choose_to_enter_numOfSimulations = bool(int(input("""Do you want to enter number of simulations? Enter 1(Yes) or 0(No)\n""")))
    
    if choose_to_enter_numOfSimulations:
        num_sims = int(input("Enter the number of simulations: "))
        tic = time.time()
        d = simulate(A,num_sims)
        toc = time.time()
        print(toc-tic)
    else:
        d = simulate(A)
    
    # Calculating few quantities for convergence analysis
    n = len(A) # total number of elements in A
    maj = get_majority_elem(A)[0] # maj is the majority element present in A
    m = sum([(maj == elem) for elem in A]) # number of occurences of the majority element "maj" in A
    print(f"\nMajority element is {maj}\n")
    #Visualization for convergence analysis
    visualize(d,m,n)
    
