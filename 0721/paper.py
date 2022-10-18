# hw4
def all_list_sum(LIST):
    result = 0
    for list in LIST:
        for num in list:
            result = result + num

    return result

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))

