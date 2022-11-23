# -*- coding: utf-8 -*-
import secrets
from multiprocessing import Pool

from identity.constants import *


class GenerateUniqueID:

    def generate_alphanumeric_unique_id(self):
        '''
        generates the alphanumeric unique id with length 7
        :return unique_id:
        '''
        try:
            return ''.join(secrets.choice(ID_CHARACTERS) for _ in range(UNIQUE_ID_LENGTH))
        except Exception as exc_msg:
            self.generate_alphanumeric_unique_id()  # recursive

    def bulk_generation_of_unique_ids(self, number_of_unique_ids):
        '''
        it generates the unique ids in bulk for given number
        when we request one million unique ids, i see some duplicates has come
        to avoid that, used while loop, until the condition of length of generated ids matches the given number
        it keep on calls generate unique id method
        '''

        set_unique_ids = set()

        while len(set_unique_ids) != number_of_unique_ids:
            unique_id = self.generate_alphanumeric_unique_id()
            set_unique_ids.add(unique_id)

        return list(set_unique_ids)

    def generate_unique_ids_in_multi_thread_env(self, number_of_unique_ids):
        '''
        multi processing
        Used process pool to get the returned unique id values from the method
        if we go with the process method, it is little difficult to collect return arguments
        With this approach, the method is showing high performance when compared to sigle thread process (bulk generation)

        In multiple processes, the unique ids are generated independently but there is a scope to get
        duplicate ids across the process.
        but with in the process, it gives unique ids

        return ids will be unique, removing duplicates
        '''

        with Pool(4) as p:
            results = p.map(self.bulk_generation_of_unique_ids, [number_of_unique_ids / 4 for _ in range(4)])

        list_unique_ids = []
        [list_unique_ids.extend(items) for items in results]

        return set(list_unique_ids)

