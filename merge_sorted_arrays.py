import pdb

def merge(input1: list, input2: list) -> list:
    merging = input1 + input2
    merging.sort()
    rmv_dups = set(merging)
    # pdb.set_trace()
    merged = []
    for ec in rmv_dups: merged.append(ec)
    print(merged)

# array1 = [1,4,6,2,9]
array1 = [21,4,6,12,9,13]
array2 = [21,12,13]

merge(array2, array1)