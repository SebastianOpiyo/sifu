'''
Print all subsequences of a string in Python
Given a string, we have to find out all subsequences of it.
A String is a subsequence of a given String, that is generated by 
deleting some character of a given string without changing its order.

Examples: 
Input : abc ->  a, b, c, ab, bc, ac, abc
Input : aaa -> a, aa, aaa
'''


def getSubsequences(s):
    subsequences = []

    def helper(s, i, subsequence):
        if len(s) == i:
            subsequences.append(subsequence)
        else:
            helper(s, i+1, subsequence + s[i])
            helper(s, i+1, subsequence)

    helper(s, 0, '')
    return subsequences
