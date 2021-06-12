# @dingzhihui   
# 2021/5/24   
# 11:19 上午   
# PyCharm
import os

import pytest

if __name__ == '__main__':
    # -v打印类 方法名 ，-s 打印print内容
    # pytest.main(['-sv'])
    # 执行模块运行
    # pytest.main(['-sv', 'test_login.py'])
    # 指定运行文件夹下的所有测试用例
    # pytest.main(['-sv', '/Users/dingzhihui/PycharmProjects/test_python_pytest/interFace'])
    # 根据nodeid执行测试用例  /Users/dingzhihui/PycharmProjects/test_python_pytest
    # pytest.main(['-sv', '../interFace/interface_test.py::test_o1_func'])
    # 失败的用例重新再跑2次
    # pytest.main(['-sv', '../testCase', '--reruns=2'])
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')
