import requests
import rsa
import base64
import urllib.parse

def rsaEncrypt(str):
    (pubkey,privkey) =rsa.newkeys(512) #生成公钥、私钥
    # print("公钥:\n%s\n私钥:\n%s" % (pubkey, privkey))
    content=str.encode('utf-8')  #明文编码格式
    crypto=rsa.encrypt(content,pubkey)  #公钥加密
    return (crypto,privkey)

str, pk = rsaEncrypt("15194779206")
print(str)#加密后密文

def base64Encode(data):
    # pwd = data
    pwdencode = base64.b64encode(data.encode('utf-8'))
    newPWD = bytes.decode(pwdencode)
    # data = newPWD
    return newPWD
str ="b'\x859\xd3WM\x86V_\xb2\xff\x95w\xe7z=\xf1\x05\x02L\xc4 |\xd4\xb1\xae\x9e-f)\xef\x13\x06\xf4n\xadr\xefyb\xbbEC}Kp\xafi\x02J\xf6(i\x1fQ\x0c\xc8\xe3\xcc\xcf\xf3\xa8\x9dy\\'"
basedata = base64Encode(str)
print(basedata)


datas = {"wd":basedata}
tedu = urllib.parse.quote(datas)
print(tedu)


Login_url = "https://test.kapbook.cn/login/check_login_ajax"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
Login_data = {
    'email': "iPHIeyR1NdYJdyg%252FziANoMoqUac6JvN%252FNbFKlCUyAIlc7qJ7JSbse434fldIJut1YQ%252BcEtddqml%252FqxEr98Te%252FLW1L0UgLLN4Kh6dlCO2blInxWZt54EZ0YawjGneRev2qUQ2lvE84nq3f9QveS2GVVQ7nMvSo68h2OpFV%252BNO6Ko%253D",
    'password': "khQJx68MvHHDF%252Fw2%252BVtB5%252BP15cgP5uOUn7PCcwX%252FndRlB0wkOInxF27QyIPtfCGx9%252FMk3pTyxTJ6QTr16OTaGbIN2mxzQyKhJNZYxUo2lt%252F3TN4TjM38Kcaa2pgaCsf9Vi49YiD7ugpUG9BEB811QkG%252F%252BVFKyW%252BkiV0l5Am6ipY%253D",
    'type': "1"
}
response = requests.post(url=Login_url,data=Login_data,headers=header)
print(response.text)