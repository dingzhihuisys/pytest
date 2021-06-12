# @dingzhihui   
# 2021/5/24   
# 3:00 下午   
# PyCharm

# def test_o1_func():
#     print("测试nodeid执行")
import pytest


class TestInterFace:
    # @pytest.mark.parametrize('args', ['测试01', '测试02', '测试03'])
    # def test_interFace_01(self, args):
    #     print(args+"调用成功")
    #
    # @pytest.mark.parametrize('args', [['dingzhihui01', 'dingzhihuiu02', 'dingzhihui03'], ['zhaoli01', 'zhaoli02', 'zhaoli03']])
    # def test_interFace_01(self, args):
    #     print(args)

    # 解包
    @pytest.mark.parametrize('args,name', [['dingzhihui01', 'dingzhihui03'], ['zhaoli01', 'zhaoli03']])
    def test_interFace_01(self, args, name):
        print(args, name)