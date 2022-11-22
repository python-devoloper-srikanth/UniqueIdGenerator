# -*- coding: utf-8 -*-

from identity.constants import *


def test_generate_unique_id_inputs_are_valid():
    '''
    assets - the constant module is errorless
    :return:
    '''
    assert UNIQUE_ID_LENGTH == 7
    assert ID_CHARACTERS == '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
