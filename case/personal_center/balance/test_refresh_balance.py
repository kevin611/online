import unittest
from common import base, logger, get_token
from data.readexcel import ExcelUtil

data = ExcelUtil("personal_center").dict_data() # 读取登出数据
class RefreshBalance(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()
	def test_refresh_balance(self):
		'''刷新会员余额'''
		route = data[1]["route"]
		url = "".join(base.get_url(route))
		Method = data[1]["method"]
		headers = {"Authorization":self.token}
		kwargs = {"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertIn(resp.json()["message"].replace("'\'","'\\'"),data[1]["expect"],msg="失败原因为%s not in %s" % (resp.json()["message"].replace("'\'","'\\'"), data[1]["expect"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()