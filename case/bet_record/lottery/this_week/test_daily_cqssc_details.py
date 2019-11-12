import unittest
from common import base, logger,get_token
from data.readexcel import ExcelUtil
from case.bet_record.lottery.this_week import get_this_week_list

data = ExcelUtil("betrecord").dict_data()
class BetRecordCqssc(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
	def test_cqssc_bet_details_daily(self):
		'''测试获取本周每天的欢乐生肖投注详情'''
		route = data[18]["route"]
		url = "".join(base.get_url(route))
		Method = data[18]["method"]
		params = eval(data[18]["params"])
		res = get_this_week_list.BetRecord().get_betrecord_list().json()["data"]["list"]  # 获取查询时间
		for d in res:
			date = d["date"]["date"]
			params["date"] = date
			headers = {"Authorization": get_token.GetRes().get_res()}
			kwargs = {"params": params, "headers": headers}
			resp = base.get_response(url,Method,**kwargs)
			self.log.info("----------test is start----------")
			self.log.info("请求的接口地址为: %s" % resp.url)
			self.log.info("请求的参数为: %s" % kwargs)
			self.log.info("响应内容为: %s" % resp.json())
			self.log.info("响应状态码为: %s" % resp.status_code)
			self.assertEqual(data[18]["expect"],resp.json()["message"],msg="失败原因为%s != %s" % ( data[18]["expect"],resp.json()["message"]))
			self.log.info("----------test is pass----------")
			self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()