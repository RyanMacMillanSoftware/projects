'''
You are given a 0-indexed string s and a 0-indexed integer array spaces that 
describes the indices in the original string where spaces will be added. Each 
space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces 
before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain 
"Enjoy Your Coffee".

Return the modified string after the spaces have been added.
'''

from typing import List


def add_spaces_iterative(s: str, spaces: List[int]) -> str:
    '''
    Idea 1: just build the string iteratively
    
    Beats 21.28% runtime, 35.18% in memory
    '''
    spaces_i = 0
    
    result = ""
    for s_i, s_val in enumerate(s):
        if spaces_i < len(spaces) and spaces[spaces_i] == s_i:
            result += " "
            spaces_i += 1
        result += s_val
    
    return result


def add_spaces_list(s: str, spaces: List[int]) -> str:
    '''
    Idea 2: construct a character list then join into a string
    
    Beats 40.53% runtime and 36.87% in memory
    '''
    spaces_i = 0
    
    result = []
    for s_i, s_val in enumerate(s):
        if spaces_i < len(spaces) and spaces[spaces_i] == s_i:
            result.append(" ")
            spaces_i += 1
        result.append(s_val)
    
    return "".join(result)




def add_spaces(s: str, spaces: List[int]) -> str:
    '''
    Idea 2: 
    construct a character list, 
    but this time declare it at the correct length upfront,
    then join into a string
    
    Beats 32.36% runtime and 71.57% in memory
    '''
    result_i = 0
    spaces_i = 0
    
    result = [0] * (len(s) + len(spaces))
    for s_i, s_val in enumerate(s):
        if spaces_i < len(spaces) and spaces[spaces_i] == s_i:
            result[result_i] = " "
            result_i += 1
            spaces_i += 1
        result[result_i] = s_val
        result_i += 1
    
    return "".join(result)