# d = ["Bob", "Ivan", 0, "MAXXXXXXXXXX"]

def out_func(string):
    for i in range(len(string)):
        if len(string) == 0:
            return "No likes"
        elif len(string) == 1:
            result = f'{string[0]}  liked it'
            return result
        elif len(string) == 2:
            result = f'{string[0]} and {string[1]} liked it'
            return result
        elif len(string) == 3:
            result = f'{string[0]}, {string[1]} and {string[2]} liked it'
            return result
        elif len(string) >= 4:
            result = f'{string[0]}, {string[1]} and other {len(string)-2} person liked it'
            return result




# print(out_func(d))
