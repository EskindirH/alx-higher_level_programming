#!/usr/bin/python3
def multiple_returns(sentence):
    len_st = len(sentence)
    if len_st == 0:
        new_tuple(len_st, None)
    else:
        new_tuple(len_st, sentence[0])
    return new_tuple    
