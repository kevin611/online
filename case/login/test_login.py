import unittest,pytesseract,PIL.ImageOps,base64,time,random,string,os,requests
from common import base, logger,cof
from data.readexcel import ExcelUtil
from PIL import Image


data = ExcelUtil("login").dict_data() # 读取登录数据
class Login(unittest.TestCase):
	'''测试会员登录'''
	def setUp(self):
		self.log = logger.Log() # 实例化日志
	def test_login(self,threshold=120):
		route = data[0]["route"]
		url = "".join(base.get_url(route))
		Method = data[0]["method"]
		json_data = eval(data[0]["data"])

		# ------获取验证码------
		code_url = cof.get_codeurl() # 获取验证码链接
		while True:
			res = requests.get(code_url).json()["data"]
			captcha_image_text = res["captcha_image_text"].split(',')[1]  # 获取图片
			image_data = base64.b64decode(captcha_image_text) # 图片解码
			img_path = os.path.dirname(os.path.dirname(__file__)) + "/code.jpeg" # 保存到本地
			with open(img_path, 'wb') as f:
				f.write(image_data)
			table = []
			for i in range(256):
				if i < threshold:
					table.append(0)
				else:
					table.append(1)
			im = Image.open(img_path)
			# 图片的处理过程
			im = im.convert('L')
			binaryImage = im.point(table, '1')
			im1 = binaryImage.convert('L')
			im2 = PIL.ImageOps.invert(im1)
			im3 = im2.convert('1')
			im4 = im3.convert('L')
			# 将图片中字符裁剪保留
			box = (10, -5, 135, 50)
			region = im4.crop(box)
			# 将图片字符放大
			out = region.resize((200, 60))
			code = pytesseract.image_to_string(out)  # 验证码
			if len(code) != 4:
				print("验证码获取错误%s，正在重新获取..." % code)
				time.sleep(1)
				continue
			elif random.choice(string.ascii_letters + '/\{}[]?<>,.!@#$%^&*() +=-_') in code:
				print("验证码获取错误%s，正在重新获取..." % code)
				time.sleep(1)
				continue
			else:
				break
		captcha_key = res["captcha_key"]
		json_data["code"] = code # 验证码
		json_data["captcha_key"] = captcha_key
		kwargs = {"json": json_data}
		resp = base.get_response(url, Method, **kwargs)
		self.log.info("----------test is start----------")
		self.log.info("请求的接口地址为: %s" % url)
		self.log.info("请求的参数为: %s" % kwargs)
		self.log.info("响应内容为: %s" % resp.text)
		self.log.info("响应状态码为: %s" % resp.status_code)
		self.assertIn(data[0]["expect"], resp.json()["message"].replace("'\'","'\\'"), msg="失败原因为%s not in %s" % (data[0]["expect"], resp.json()["message"].replace("'\'","'\\'"))) # 响应结果转义成中文
		self.log.info("----------test is pass----------")
		self.log.info("----------test is end----------")


if __name__ == "__main__":
	unittest.main()