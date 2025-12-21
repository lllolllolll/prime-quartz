import requests
from bs4 import BeautifulSoup
import json
import os
import re

# 网站URL
base_url = 'https://www.chem.pku.edu.cn/zxyu/publications/index.htm'

# 保存图片的目录
image_dir = 'F:/work/prime-quartz_unzipped/prime-quartz-main/content/publications/picture'

# 确保图片目录存在
os.makedirs(image_dir, exist_ok=True)

# 从web_reference中获取的文献数据
web_content =