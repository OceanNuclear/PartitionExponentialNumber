"""
Consider the following question:
'Can all even numbers be uniquely expressed as a sum of powers of two, without using each powers of two more than once.'
E.g.
18=16*1+8*0+4*0+2*1 (therefore the answer is yes for 18)
We can generalize the question to:
"For a chosen number n, can all positive integers be uniquely expressed as a sum of g*n^k's, where 0<=g<n, k>1, and all g, n, k are integers."
I suspect the answer is yes after thinking about modular arithmatic for a bit,
but I'll verify it with this python script
"""
import itertools as it
import numpy as np
from numpy import array as ary

def all_possible_g_vector(n, max_exponent):
    return it.product(*[range(n) for _ in range(max_exponent)])

def partition_number_as_powers_of_n(number, n):
    """See if a positive integer can be represented as a g-vector."""
    max_k = 0
    while n**(max_k)<=number:
        max_k+=1

    for choice_vector in all_possible_g_vector(n,max_k):
        # choice_vector is 'g' as defined in the doc-string above.
        sum(ary(choice_vector) * ary([n**i for i in reversed(range(max_k))]))

def check_if_npartitions_are_unique(n, up_to_exponent):
    input_output = {}
    for choice_vector in all_possible_g_vector(n,up_to_exponent):
        input_output[choice_vector] = sum(ary(choice_vector) * ary([n**i for i in reversed(range(up_to_exponent))]))
    return input_output

if __name__=='__main__':
    # partition_number_as_powers_of_n(15,3)
    import sys
    n = int(sys.argv[1])
    max_exponent = int(sys.argv[2])
    ndict = check_if_npartitions_are_unique(n, max_exponent)
    assert len(ndict)==len(set(list(ndict.values())))

"""The answer is yes, for all of the single digit integers up to max_exponent=5 that I've checked."""