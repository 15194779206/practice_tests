import base64

def base64Encode(data):
    pwd = data['password']
    pwdencode = base64.b64encode(pwd.encode('utf-8'))
    newPWD = bytes.decode(pwdencode)
    data['password'] = newPWD
    return data

