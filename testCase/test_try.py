# @dingzhihui   
# 2021/6/2   
# 2:42 下午   
# PyCharm
import pytest

class TestTry:
    def test_find_largest_element(l):
        if not isinstance(l, list):
            print('input is not type of list')
            return
        if len(l) == 0:
            print('empty input')
            return
        largest_element = l[0]
        for item in l:
            if item > largest_element:
                largest_element = item
        print('largest element is: {}'.format(largest_element))

    test_find_largest_element([8, 1, -3, 2, 0])



