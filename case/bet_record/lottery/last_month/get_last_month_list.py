import datetime
from common import base,get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("betrecord").dict_data()
class BetRecord():
	def __init__(self):
		self.token = get_token.GetRes().get_res()

	def get_betrecord_list(self):
		'''获取月彩票注单列表'''
		route = data[63]["route"]
		url = "".join(base.get_url(route))
		Method = data[63]["method"]
		params = eval(data[63]["params"])
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

		params["time_start"] = start
		params["time_end"] = end
		headers = {"Authorization": self.token}
		kwargs = {"params": params, "headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		return resp

