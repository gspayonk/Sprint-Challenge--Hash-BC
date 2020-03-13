#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    indices = None
    for i, w in enumerate(weights):
        if hash_table_retrieve(ht, w) is not None:
            indices = [i, hash_table_retrieve(ht, w)]
            if indices[1] > indices[0]:
                indices[0], indices[1] = indices[1], indices[0]
        else:
            hash_table_insert(ht, limit-w, i)
    return indices


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
