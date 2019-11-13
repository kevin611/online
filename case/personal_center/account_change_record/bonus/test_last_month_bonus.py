import unittest,datetime
from common import base, logger,get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("personal_center").dict_data()
class Bonus(unittest.TestCase):
	'''获取上月优惠记录'''
	def setUp(self):
		self.log = logger.Log()
		self.token = get_token.GetRes().get_res()

	def test_bonus_lastmonth(self):
		route = data[16]["route"]
		url = "".join(base.get_url(route))
		Method = data[16]["method"]
		headers = {"Authorization": self.token}
		params = eval(data[16]["params"])
		# 获取当前日期
		date = datetime.datetime.now()
		year = date.year
		month = date.month
		if month == 1:
			start = datetime.date(year - 1, 12, 1)
		else:
			start = datetime.date(year, month - 1, 1)
		end = datetime.date(year, month, 1) - datetime.timedelta(days=1)
		params["time_start"] = start
		params["time_end"] = end
		kwargs = {"params":params,"headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertIn(resp.json()["message"].replace("'\'","'\\'"),data[16]["expect"],msg="失败原因为%s not in %s"%(resp.json()["message"].replace("'\'","'\\'"), data[16]["expect"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")

if __name__ == "__main__":
	unittest.main()