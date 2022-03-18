import pdb
import time

def first_recurring_char(arr: list):  
    start_time = time.time()

    tracker = dict()    

    for ec in arr:
        if ec in tracker:
            print(ec)
            return ec
        else:
            tracker[ec] = None

  
    # pdb.set_trace()
    # tracker = list()
    # # arr = arr[1:len(arr)-1].split(",")

    # for ec in arr:
    #     if ec in tracker:
    #         print(ec)
    #         return ec
    #     else:
    #         tracker.append(ec)

    print(f"{time.time() - start_time} milliseconds")
    return None

# list_input = input()

        # Test Cases
# list_input = [1,2,3,4]
# list_input = []
# list_input = [1,2]
# list_input = [1,1,2]
# list_input = [1,2,1,2]
# list_input = [1,2,2,1]
# list_input = [1,2,3,4,5,6,7,7,3]
list_input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

first_recurring_char(list_input)

