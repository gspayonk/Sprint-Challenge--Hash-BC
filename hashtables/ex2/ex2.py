#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    the_list = []

    for i in tickets:
        if i.source == 'NONE':
            s = i
        if i.destination == 'NONE':
            e = i

    first_leg = s.destination
    while first_leg != 'NONE':
        for i in tickets:
            if i.source == first_leg:
                hash_table_insert(hashtable, i.source, i.destination)
                the_list.append(i.source)
                first_leg = i.destination
            hash_table_insert(hashtable, e.source, e.destination)
        
    return the_list



