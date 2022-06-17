# d = ["Bob", "Bpbby", "Kate", 'Max']


def check_list_str(inlist):
    if all([isinstance(item, str) for item in inlist]):
        return False
    else:
        return True


def check_element_alpha(delement):
    for i in range(len(delement)):
        dx = str(delement[i])
        x = all([item.isalpha() for item in dx])
        if not x:
            return True


def check_item_len(g):
    for i in range(len(g)):
        g1 = str(g[i])
        if len(g1) > 10:
            return True


def global_check(x):
    check_result = [check_item_len(x), check_element_alpha(x), check_list_str(x)]
    if True in check_result:
        return True, 'You made mistake in name, try again'

#
# print('len', check_item_len(d))
# print('is str', check_list_str(d))
# print('is elements alpha', check_element_alpha(d))
# print(global_check(d))
