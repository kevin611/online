import unittest
from common import logger
from data.readexcel import ExcelUtil
from case.bet_record.lottery.this_month import get_this_month_list

data = ExcelUtil("betrecord").dict_data()
class BetRecordList(unittest.TestCase):
	'''测试获取视讯本月投注记录'''
	def setUp(self):
		self.log = logger.Log()
	def test_get_livelist_this_month(self):
		res = get_this_month_list.BetRecord().get_betrecord_list() # 本月视讯投注记录
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为 %s" %res.url)
		self.log.info("响应内容为: %s" % res.json())
		self.log.info("响应状态码为: %s" % res.status_code)
		self.assertEqual(data[110]["expect"],res.json()["message"],msg="失败原因%s ！= %s"%(data[110]["expect"],res.json()["message"]))
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")

if __name__ == "__main__":
	unittest.main()
