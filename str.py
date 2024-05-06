import re

# 打开本地文档
with open('C:/Users/m/Desktop/dtap.xml', 'r') as f:
    content = f.read()

# 提取所有字符串
strings = re.findall(r'\b[\w-]+\b', content)

# 将结果输出到文件
with open('C:/Users/m/Desktop/dtap.txt', 'w') as f:
        for string in strings:
            f.write(string + '\n')
