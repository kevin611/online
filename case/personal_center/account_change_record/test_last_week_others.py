import unittest,time,datetime
from common import base, logger,get_token
from data.readexcel import ExcelUtil

data = ExcelUtil("personal_center").dict_data()

class Others(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()

	def test_others_lastweek(self):
		'''获取上周其他记录'''
		route = data[22]["route"]
		url = "".join(base.get_url(route))
		Method = data[22]["method"]
		headers = {"Authorization": self.token}
		params = eval(data[22]["params"])
		today = datetime.date.today()
		params["time_start"] = today - datetime.timedelta(days=today.weekday()+7) # 上周一，开始时间
		params["time_end"] = today - datetime.timedelta(days=today.weekday()+1) # 上周日，结束时间
		kwargs = {"params":params,"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertIn(resp.json()["message"].replace("'\'","'\\'"),data[22]["expect"],msg="失败原因为%s not in %s"%(resp.json()["message"].replace("'\'","'\\'"), data[22]["expect"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")

if __name__ == "__main__":
	unittest.main()