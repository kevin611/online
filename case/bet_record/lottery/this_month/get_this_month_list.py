import datetime
from common import base,get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("betrecord").dict_data()
class BetRecord():
	def __init__(self):
		self.token = get_token.GetRes().get_res()

	def get_betrecord_list(self):
		'''获取本周彩票注单列表'''
		route = data[0]["route"]
		url = "".join(base.get_url(route))
		Method = data[0]["method"]
		params = eval(data[0]["params"])
		# 获取当前日期
		date = datetime.datetime.now()
		year = date.year
		month = date.month
		today = datetime.date.today() # 今日
		# 开始日期
		start = datetime.date(year, month, 1)
		# 结束日期
		if month == 12:
			end = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
		else:
			end = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

		params["time_start"] = start
		params["time_end"] = today
		headers = {"Authorization": self.token}
		kwargs = {"params": params, "headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		return resp

