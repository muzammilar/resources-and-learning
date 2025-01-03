# m+n instead of n*m, open ended, can do that or save space
def sumOfTwo(a, b, v):
    set_a = set(a)
    set_b = set(b)
    for x in set_b:
        if (v - x) in set_a:
            return True
    return False


"""

You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
sumOfTwo(a, b, v) = true.

Input/Output

    [time limit] 4000ms (py)

    [input] array.integer a

    An array of integers.

    Guaranteed constraints:
    0 ≤ a.length ≤ 105,
    -109 ≤ a[i] ≤ 109.

    [input] array.integer b

    An array of integers.

    Guaranteed constraints:
    0 ≤ b.length ≤ 105,
    -109 ≤ b[i] ≤ 109.

    [input] integer v

    Guaranteed constraints:
    -109 ≤ v ≤ 109.

    [output] boolean

    true if there are two elements from a and b which add up to v, and false otherwise.


"""