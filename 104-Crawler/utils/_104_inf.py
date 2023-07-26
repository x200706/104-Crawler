from collections import namedtuple
import urllib.parse

_104_URL = 'https://www.104.com.tw/'

SEARCH_URL = urllib.parse.urljoin(_104_URL, 'jobs/search/list')

headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
  'Connection': 'keep-alive',
  'Host': 'www.104.com.tw',
  'Referer': 'https://www.104.com.tw/jobs/search/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

requirement = namedtuple('requirement', [
  'ro', 'keyword', 'jobcatExpansionType', 'area', 'edu', 'sctp', 'scmin',
  'scmax', 'scstrict', 'jobexp', 'jobsource', 'page'
])
# 擴大搜尋範圍減少過濾
nrequirement = namedtuple('requirement',
                          ['ro', 'keyword', 'area', 'sctp', 'scmin', 'page'])

df_template = {
  "jobName": "",
  "salaryLow": "",
  "salaryHigh": "",
  "appearDate": "",
  "jobAddrNoDesc": "",
  "jobAddress": "",
  "applyDesc": "",
  "custName": "",
  "coIndustryDesc": ""
}