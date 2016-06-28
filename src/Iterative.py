

def calc_my_start_value(indices, my_index, min_index_value, max_index_value):
    value = None
    if my_index > 0:
        if indices[my_index-1] + 1 <= max_index_value:
            value = indices[my_index-1]+1
    else:
        value = min_index_value
    if value:
        indices[my_index] = value


def calc_my_next_value(indices, my_index, max_index_value):
    if indices[my_index] + 1 <= max_index_value:
        indices[my_index] += 1
        return True
    else:
        return False

i2 = [0,0,0,0]
for x in range(len(i2)):
    calc_my_start_value(i2, x, 1, 10)
print(i2)

while calc_my_next_value(i2, 2, 10):
    print(i2)