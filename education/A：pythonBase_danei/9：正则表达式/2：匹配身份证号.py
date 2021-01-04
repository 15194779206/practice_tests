import re

test = re.search('\d{17}(\d|x)', '13108200001011050x').group()
print(test)