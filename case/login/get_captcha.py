import requests
import pytesseract,PIL.ImageOps,base64,time,random,string,os
from PIL import Image

def get_captcha(threshold=120):
	url = "http://klk.9161252.com/frontend/v1/captcha?userName=test0001"
	while True:
		res = requests.get(url).json()["data"]
		captcha_image_text = res["captcha_image_text"].split(',')[1] # 获取图片
		image_data = base64.b64decode(captcha_image_text)
		img_path = os.path.dirname(os.path.dirname(__file__)) + "/1.jpeg"
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
		code = pytesseract.image_to_string(out) # 验证码
		if len(code) != 4 or random.choice(string.ascii_letters + '/\{}[]?<>,.!@#$%^&*() +=-_') in code:
			print("验证码获取错误%s，正在重新获取..." %code)
			time.sleep(3)
			continue
		else:
			break
	# code = pytesseract.image_to_string(out) # 验证码
	captcha_key = res["captcha_key"]
	# print(out.show())
	return code

