# -*- coding: utf-8 -*-
import re
import time

import pytest

from identity.constants import *
from identity.generation import GenerateUniqueID

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture()
def generate_unique_id():
    '''
    fixture
    :return 'GenerateUniqueID' class object:
    '''
    return GenerateUniqueID()


def test_unique_id_is_of_correct_length(generate_unique_id):
    '''
    asserts - length of unique id is 7 or not
    :param unique_id:
    :return:
    '''
    unique_id = generate_unique_id.generate_alphanumeric_unique_id()
    assert len(unique_id) == UNIQUE_ID_LENGTH


def test_unique_id_uses_correct_characters(generate_unique_id):
    '''
    asserts - the generated unique id is alphanumeric
    :param unique_id:
    :return:
    '''
    unique_id = generate_unique_id.generate_alphanumeric_unique_id()
    re_pattern = '^[A-Z0-9]+$'
    check = re.compile(re_pattern)
    assert check.match(unique_id) is not None


def test_bulk_generation_of_unique_ids(generate_unique_id):
    '''
    assets - bulk generation test
    :return:
    '''
    strat_time = time.perf_counter()
    number_of_unique_ids = 100000
    list_unique_ids = generate_unique_id.bulk_generation_of_unique_ids(number_of_unique_ids)
    end_time = time.perf_counter()
    assert len(set(list_unique_ids)) == number_of_unique_ids
    print(
        f'Bulk generation - Time taken for {number_of_unique_ids} unique ids is {round(end_time - strat_time, 2)} seconds')


def test_generation_of_unique_ids_for_concurrency_in_multi_thread_env(generate_unique_id):
    '''
    assets - bulk generation of unique ids for concurrency in multi thread environment
    :return:
    '''
    strat_time = time.perf_counter()
    number_of_unique_ids = 100000
    set_unique_ids = generate_unique_id.generate_unique_ids_in_multi_thread_env(number_of_unique_ids)
    end_time = time.perf_counter()
    assert len(set_unique_ids) == number_of_unique_ids
    print(
        f'Bulk generation - Time taken for {number_of_unique_ids} unique ids is {round(end_time - strat_time, 2)} seconds')


def test_performance_between_sequential_parallel_processing(generate_unique_id):
    '''
    assets - performance test
    :return:
    '''
    number_of_unique_ids = 1000000

    strat_time1 = time.perf_counter()
    list_unique_ids = generate_unique_id.bulk_generation_of_unique_ids(number_of_unique_ids)
    end_time1 = time.perf_counter()

    sequential_processing_duration = round(end_time1 - strat_time1, 2)
    print(f'sequential_processing_duration - {sequential_processing_duration} seconds')

    strat_time2 = time.perf_counter()
    set_unique_ids = generate_unique_id.generate_unique_ids_in_multi_thread_env(number_of_unique_ids)
    end_time2 = time.perf_counter()

    multi_processing_duration = round(end_time2 - strat_time2, 2)
    print(f'multi_processing_duration - {multi_processing_duration} seconds')

    assert sequential_processing_duration > multi_processing_duration
