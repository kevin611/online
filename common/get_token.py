from common import base,cof
from data.readexcel import ExcelUtil
import pytesseract,PIL.ImageOps,base64,time,random,string,os,requests
from PIL import Image



data = ExcelUtil("login").dict_data()
class GetRes(object):
    def get_res(self,threshold=120):
        '''获取token响应'''
        while True:
            route = data[0]["route"]
            url = "".join(base.get_url(route))
            Method = data[0]["method"]
            json_data = eval(data[0]["data"])

            # ------获取验证码------
            code_url = cof.get_codeurl()
            while True:
                res = requests.get(code_url).json()["data"]
                captcha_image_text = res["captcha_image_text"].split(',')[1]  # 获取图片
                image_data = base64.b64decode(captcha_image_text)
                img_path = os.path.dirname(os.path.dirname(__file__)) + "/code.jpeg"
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
                if len(code) != 4 or random.choice(string.ascii_letters + '/\{}[]?<>,.!@#$%^&*() +=-_') in code:
                    print("验证码获取错误%s，正在重新获取..." % code)
                    time.sleep(1)
                    continue
                else:
                    break
            captcha_key = res["captcha_key"]
            json_data["code"] = code  # 验证码
            json_data["captcha_key"] = captcha_key
            kwargs = {"json": json_data}
            try:
                res = base.get_response(url, Method, **kwargs).json()["data"]
            except Exception as e:
                continue
            else:
                return res["token"]

