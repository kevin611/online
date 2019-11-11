

def get_host():
    host = "http://klk.9161252.com:801" # 客拉客 测试会员账号mmmlll
    host2 = "http://eyc.9161252.com:801" # 103棋牌 测试会员账号mmmlll
    host_pjdc = "http://pjdc.9161252.com" # 线上环境pjdc
    return host_pjdc


# 获取验证码URL
def get_codeurl():
    code_url1 = "http://klk.9161252.com/frontend/v1/captcha?userName=mmmlll"
    code_url2 = "http://eyc.9161252.com/frontend/v1/captcha?userName=mmmlll"
    return code_url2