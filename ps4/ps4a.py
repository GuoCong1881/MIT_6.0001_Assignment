# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    pmlist = []
    length = len(sequence)
    if length == 1:
        pmlist.append(sequence)
     
    else:
        pop_letter = sequence[-1]
        sequence_pop = sequence[0:-1]
        for each_permutation in get_permutations(sequence_pop):
            each_plist = list(each_permutation)
            for position in range(len(each_permutation)+1):
                    each_plist_copy = each_plist[:]
                    each_plist_copy.insert(position,pop_letter)
                    added_permutation = ''.join(each_plist_copy)
                    if added_permutation not in pmlist:
                        pmlist.append(added_permutation)
   
    return pmlist



if __name__ == '__main__':

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'abb'
    print('Input:', example_input)
    print('Expected Output:', ['abb', 'bba', 'bab'])
    print('Actual Output:', get_permutations(example_input))
    




