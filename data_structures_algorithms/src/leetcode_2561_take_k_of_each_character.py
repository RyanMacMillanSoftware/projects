'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. 
Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, 
or return -1 if it is not possible to take k of each character.

https://leetcode.com/problems/take-k-of-each-character-from-left-and-right
'''

def solution(s: str, k: str) -> int:
    '''
    Idea 1L
    O(s)
    Count all a's, b's and c's. 
    O(s)
    Move a sliding window through the string char array.
    Find maximum length sliding window that leaves atleast 2 of each character outside it's bounds
    
    Complexity: O(s)
    
    Beats 43% in runtime and 94.49% in memory.
    Can optimise the sliding window, such as how we move the left pointer, but won't do. 
    '''
    if k <= 0:
        return 0
    count = [0,0,0]  # a, b, c
    for char in s:
        count[ord(char) - ord('a')] += 1
    for n in count:
        if n < k:
            return -1
    
    l_pntr = 0
    r_pntr = 0
    max_window_size = 0
    while l_pntr < len(s) and r_pntr < len(s):
        while r_pntr < len(s) and k-1 not in count:
            new_window_char = s[r_pntr]
            count[ord(new_window_char) - ord('a')] -= 1
            if k-1 not in count:
                window_size = r_pntr - l_pntr + 1
                max_window_size = max(window_size, max_window_size)
            r_pntr += 1
            
        while l_pntr < len(s) and k-1 in count and l_pntr <= r_pntr:
            new_window_char = s[l_pntr]
            count[ord(new_window_char) - ord('a')] += 1
            l_pntr += 1
    
    return len(s) - max_window_size    
