import datetime
from common import base,get_token
from data.readexcel import ExcelUtil


data = ExcelUtil("betrecord").dict_data()
class BetRecord():
	def __init__(self):
		self.token = get_token.GetRes().get_res()

	def get_betrecord_list(self):
		'''获取上周体育注单列表'''
		route = data[194]["route"]
		url = "".join(base.get_url(route))
		Method = data[194]["method"]
		params = eval(data[194]["params"])
		today = datetime.date.today()
		params["time_start"] = today - datetime.timedelta(days=today.weekday() + 7)  # 上周一，开始时间
		params["time_end"] = today - datetime.timedelta(days=today.weekday() + 1)  # 上周日，结束时间
		headers = {"Authorization": self.token}
		kwargs = {"params": params, "headers": headers}
		resp = base.get_response(url, Method, **kwargs)
		return resp


