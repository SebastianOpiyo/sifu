def reverse_str(s):
    reversedString = ''
    index = len(str) # calculate length of string and save in index

    while index > 0: 
        reversedString += str[index - 1] # save the value of str[index-1] in reverseString
        index = index - 1 # decrement index
    print(reversedString) 

def swap(s, i, j):
    strlst = list(s)
    temp = strlst[i]
    strlst[i] = strlst[j]
    strlst[j] = temp
    return "".join(strlst)

def reverse(s):
    i = 0
    j = len(s) - 1

    while (i < j):
        swap(s, i, j)
        i += 1
        j -= 1

print(reverse('hello'))
