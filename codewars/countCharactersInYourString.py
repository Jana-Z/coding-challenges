def count(string):
    # The function code should be here
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result
    
    #link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/solutions/python
