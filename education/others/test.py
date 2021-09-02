from Crypto.PublicKey import RSA
import rsa
import base64
import urllib.parse
import requests
publicKye = '''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3//sR2tXw0wrC2DySx8vNGlqt3Y7ldU9+LBLI6e1KS5lfc5jlTGF7KBTSkCHBM3ouEHWqp1ZJ85iJe59aF5gIB2klBd6h4wrbbHA2XE1sq21ykja/Gqx7/IRia3zQfxGv/qEkyGOx+XALVoOlZqDwh76o2n1vP1D+tD3amHsK7QIDAQAB
-----END PUBLIC KEY-----'''
pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(publicKye.encode())
# 加密
def jiami(message):
    content = message.encode("utf-8")
    c = rsa.encrypt(content, pubKey)
    info = base64.b64encode(c)
    result = urllib.parse.quote(info)
    return result


url = "https://test.kapbook.cn/login/check_login_ajax"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
Login_data = {
    'email': jiami("15001253128"),
    'password': jiami("123456"),
    'type': "1"
}
response = requests.post(url=url,data=Login_data,headers=header)
print(response.text)