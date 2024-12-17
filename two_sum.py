def two_sum(numbers, target):
    # takes a list of integers and a target integer. It should return the indices of the two numbers in the list that add up to the target.
    for i, v in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            if numbers[j] + v == target:
                return [i, j]
    raise ValueError("bruh")