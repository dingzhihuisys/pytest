# @dingzhihui   
# 2021/5/31   
# 11:33 上午   
# PyCharm
import json

import requests

class RequestUlr:
    # 类变量：通过类名访问
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        # 把请求类型统一转化为小写
        method = str(method).lower()
        # requests.get()
        rep = None
        if method == 'get':
            rep = RequestUlr.session.request(method, url=url, params=data, **kwargs)
        else:
            # 把data转换字符串格式
            data = json.dumps(data)
            rep = RequestUlr.session.request(method, url=url, data=data, **kwargs)
        return rep.text




