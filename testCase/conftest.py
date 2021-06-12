# @dingzhihui   
# 2021/5/27   
# 3:17 下午   
# PyCharm
import pytest

@pytest.fixture(scope="function", params=['丁智慧01', '丁智慧02', '丁智慧03', '丁智慧04'], ids=['001', '002', '003', '004'])
def test_fixture(request):
    print("这里是前置方法")
    # yield     # yield  和  return  不可以一起使用 ！！！！！！！！！！！
    # print("这里是后置方法")
    # return request.param
    yield request.param
    print("这里是后置方法")