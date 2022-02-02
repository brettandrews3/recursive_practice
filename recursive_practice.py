# Practice with recursive cases
marbles = [10, 13, 39, 14, 41, 9, 3]

def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum = first + recursive_compute_sum(rest)
        return sum

sum = recursive_compute_sum(marbles)
print('The total is', sum)


# Next, we'll try testing for palindromes with recursive case:
def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            # recursion stuff
        
        
        else:
            return False