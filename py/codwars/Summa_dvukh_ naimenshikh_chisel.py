massiv = [-10, 343445353.6, 3453445, 3453545353453]


def sum_two_smallest_numbers(numbers):
    k = a1 = a2 = 0
    numbers.sort()
    for num in range(len(numbers)):
        if numbers[num] < 0 or True != isinstance(numbers[num], int):
            continue
        elif k == 0:
            a1 = numbers[num]
            k += 1
        else:
            a2 = numbers[num]
            break
    return a1 + a2

def sum_two_smallest_numbers1(numbers):
    return sum(sorted(numbers)[:2]) if numbers else None

print(sum_two_smallest_numbers(massiv))
print(sum_two_smallest_numbers1(massiv))