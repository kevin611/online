import unittest
from common import base, logger
from data.readexcel import ExcelUtil
from case.bet_record.sport.last_week import get_last_week_list


data = ExcelUtil("betrecord").dict_data()
class BetRecordList(unittest.TestCase):
	def setUp(self):
		self.log = logger.Log()
	def test_get_sportlist_last_week(self):
		'''测试获取体育上周投注记录'''
		res = get_last_week_list.BetRecord().get_betrecord_list() # 上周体育投注记录
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为 %s" %res.url)
		self.log.info("响应内容为: %s" % res.json())
		self.log.info("响应状态码为: %s" % res.status_code)
		self.assertEqual(data[194]["expect"],res.json()["message"],msg="失败原因%s ！= %s"%(data[194]["expect"],res.json()["message"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")

if __name__ == "__main__":
	unittest.main()