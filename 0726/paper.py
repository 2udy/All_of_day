def get_dict_avg(scores):
    return sum(scores.values())/len(scores)


print(get_dict_avg({'python':80,'web':90}))