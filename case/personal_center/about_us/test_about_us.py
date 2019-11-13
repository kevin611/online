import unittest
from common import base, logger,get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("personal_center").dict_data()
class AboutUs(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()

	def test_about_us(self):
		route = data[39]["route"]
		url = "".join(base.get_url(route))
		Method = data[39]["method"]
		params = eval(data[39]["params"])
		headers = {"Authorization": self.token}
		kwargs = {"params":params,"headers":headers}
		res = base.get_response(url,Method,**kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % res.url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % res.json())
		self.log.info("响应状态码为: %s" % res.status_code)
		self.assertEqual(data[39]["expect"], res.json()["message"],
						 msg="失败原因为%s != %s" % (data[39]["expect"], res.json()["message"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")



if __name__ == "__main__":
	unittest.main()