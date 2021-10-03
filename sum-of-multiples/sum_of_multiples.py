def sum_of_multiples(limit, multiples):
    multi = [x for x in range(limit) if any(x % y == 0 for y in multiples)]
    return sum(multi)
