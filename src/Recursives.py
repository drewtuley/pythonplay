

def inc_indexes(indices, index, index_count, max_index):
    if index == index_count - 1:
        my_start = max_index
    elif index-1 >= 0:
        my_start = indices[index-1]+1
    else:
        my_start = 0

    if index < index_count-1 and my_start >= max_index:
        return

    indices[index] = my_start
    while indices[index] <= max_index:
        if index+1 < index_count:
            yield from (inc_indexes(indices, index+1, index_count, max_index))
        else:
            if indices[index_count-2] != indices[index_count-1]:
                yield(indices)
        indices[index] += 1


indexes = [0 for x in range(3)]
for x in inc_indexes(indexes, 0, len(indexes), 9):
    print(x)
