import pdb

def pair_sum(num: int, array: list) -> list:
     update_arr = list(array)
     for ec in range(len(array)):
             diff = num - array[ec]
             update_arr.pop(ec)
             if diff in update_arr:
                #      pdb.set_trace()
                     print([array[ec], diff])
                     return [array[ec], diff]
             else:
                     update_arr = list(array)

num = 8
arr = [1,2,3,4]
# arr = [1,2,4,4]
# arr = [-1,2,3,9]
# arr = [1,0,8,9]

pair_sum(num, arr)