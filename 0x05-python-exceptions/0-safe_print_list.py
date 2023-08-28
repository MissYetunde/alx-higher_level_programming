#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(i, end="")
                count += 1
        print()
        return count
    except:
        raise

# Example usage
my_list = [1, 2, 3, 4, 5]
x = 3
elements_printed = safe_print_list(my_list, x)
print("Number of elements printed:", elements_printed)
