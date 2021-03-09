import html5lib
from bs4 import BeautifulSoup

def company_token(text):
    company_dict = {}
    soup = BeautifulSoup(text, 'html.parser')
    nameList = soup.find_all(class_='enterpListName')
    tokenList = soup.find_all(class_="clickCompany")
    for i in range(len(nameList)):
        company_name = nameList[i].get('title').strip('')
        company_token = tokenList[i].get("data").strip('')
        company_dict[company_name] = company_token
    return company_dict

#
# times = response.cookies['request_time']
# tokens = response.cookies['token']
# cookie = {
#     "request_time":times,
#     "token":tokens,
# }
# company_url ="https://test.kapbook.cn/user/index?from=login"
# company_text = requests.get(url=company_url,cookies=cookie, headers=header)






