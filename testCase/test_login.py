# @dingzhihui   
# 2021/5/24   
# 10:28 上午   
# PyCharm
import pytest

class TestLogin:
    # age = 20
    def setup_class(self):
        print("在执行每个测试类之前初始化的代码：创建日志对象，创建数据量的连接，创建接口请求对象")

    def setup(self):
        print("在执行每个测试用例之前初始化的代码")

    def test_login_os01(self, test_fixture):
        print("登录01")
        print("------打印看看---"+str(test_fixture))
        # assert 1 == 2
        # --html ./report/report.html

    @pytest.mark.run(order=1)  # 执行这个用例第一个执行
    @pytest.mark.smoke
    def test_login_os02(self):
        print("登录02")

    @pytest.mark.run(order=2)
    def test_login_or03(self):
        print("登录03")

    # @pytest.mark.skipif(age >= 20, reason="有原因的跳过")
    def test_login_oi04(self):
        print("登录04")

    # @pytest.mark.usermanage
    def test_login_oi05(self):
        print("登录05")

    @pytest.mark.skip(reason="无原因的跳过")
    def test_login_oi06(self):
        print("登录06")

    def test_login_oi07(self):
        print("登录07")

    def teardown(self):
        print("在执行每个测试用例之后扫尾的代码：")

    def teardown_class(self):
        print("在执行每个测试类之后扫尾的代码----------------------")

# if __name__ == '__main__':
#     pytest.main(['-s'])
# command + /（批量注释）
