import unittest
from common import base, logger, get_token
from data.readexcel import ExcelUtil

data = ExcelUtil("personal_center").dict_data() # 读取登出数据
class MemberReport(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()
	def test_memberreport_yesterday(self):
		'''测试获取昨日个人报表'''
		route = data[26]["route"]
		url = "".join(base.get_url(route))
		Method = data[26]["method"]
		json_data = eval(data[26]["data"])
		headers = {"Authorization":self.token}
		kwargs = {"data":json_data,"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertIn(resp.json()["message"].replace("'\'","'\\'"),data[26]["expect"],msg="失败原因为%s != %s" % (resp.json()["message"].replace("'\'","'\\'"),data[26]["expect"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()