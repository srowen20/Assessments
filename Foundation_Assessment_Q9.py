# QUESTION 9: Two Number Sum

"""
 Write a function that takes in a non-empty array of distinct integers
and an integer representing a target sum. If any two numbers in the
input array sum up to the target sum, the function should return
them in an array, in any order. If no to numbers sum up to the target
sum, the function should return an empty array.
● Note that the target sum has to be obtained by summing two
different integers in the array. You cannot add a single integer to
itself in order to obtain the target sum.
● You can assume that there will be at most one pair of numbers
summing up to the target sum.
Sample Input: numbers = [3, 5, -4 ,8, 11, 1, -1, 6] target_sum = 10
Sample Output: [-1, 11] the numbers can be in any order, it does not matter
"""

num_array = [3, 5, -4 ,8, 11, 1, -1, 6]
num = 10


def two_number_sum(numbers, target_sum):
    try:
        if not numbers:
            raise Exception

        for i in range(len(numbers)-1):
            for j in range(len(numbers)-1):
                if i != j:
                    output = numbers[i] + numbers[j]
                    if output == target_sum:
                        return [numbers[i], numbers[j]]
                        break

    except:
        return 'Your array is empty'


result = two_number_sum(num_array, num)
if not result:
    print('Your numbers did not add up to', num)
else:
    print(result)




