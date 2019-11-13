import unittest
from common import base, logger, get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("personal_center").dict_data()
class Refund(unittest.TestCase):
	'''测试测试一键返水'''
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()

	def test_refund(self):
		route = data[29]["route"]
		url = "".join(base.get_url(route))
		Method = data[29]["method"]
		params = eval(data[29]["params"])
		headers = {"Authorization":self.token}
		kwargs = {"params":params,"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertEqual(data[29]["expect"],resp.json()["message"], msg="失败原因为%s != %s" % (data[29]["expect"], resp.json()["message"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()