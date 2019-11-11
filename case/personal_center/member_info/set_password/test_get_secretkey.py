import unittest
from common import base, logger, get_token
from data.readexcel import ExcelUtil

data = ExcelUtil("personal_center").dict_data()
class SecretKey(unittest.TestCase):
	'''测试获取密保问题列表'''
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()
	def test_get_secretkey(self):
		route = data[37]["route"]
		url = "".join(base.get_url(route))
		Method = data[37]["method"]
		headers = {"Authorization":self.token}
		kwargs = {"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertEqual(resp.json()["message"],data[37]["expect"], msg="失败原因为%s != %s" % (resp.json()["message"],data[37]["expect"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()