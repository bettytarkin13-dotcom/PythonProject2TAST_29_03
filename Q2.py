def find_median(number:list)->float:
    if not number:
        raise ValueError("The list is empty")

    sorted_numbers = sorted(number)
    n=len(sorted_numbers)
    middle=n//2

    if n%2==1:
        return float(sorted_numbers[middle])
    else:
        return (sorted_numbers[middle-1]+sorted_numbers[middle])/2.0

print(find_median([5, 6, 5, 1,6]))