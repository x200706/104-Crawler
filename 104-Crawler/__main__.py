# -*- coding: utf-8 -*-

from datetime import datetime
from collections import namedtuple
from option import args
from utils._104_inf import requirement, headers, df_template, SEARCH_URL

import os
import requests
import pandas as pd

current_time = "{:%Y%m%d_%H_%M}".format(datetime.now())
os.makedirs('{}/{}'.format(args.output_dir, current_time), exist_ok=True)
req = requests.Session()


def fetch(params):
  content = req.get(SEARCH_URL, params=params, headers=headers)
  return content


def run():

  print("Start crawling ...")
  # 異動處：把碩士學歷跟工作經驗的條件去掉
  init_search = requirement(1, args.key_word, '1', args.area, '', 'M',
                            args.min_salary, args.max_salary, '1', '',
                            '2018indexpoc', '1')
  init_params = dict(init_search._asdict())

  content = fetch(init_params)
  # print(content.url)
  data = content.json()

  if (data['status'] == 200):

    df_job = pd.DataFrame(columns=df_template.keys())

    totalPage = data['data'][
      'totalPage'] if args.max_page == None else args.max_page

    for page in range(totalPage):
      # 異動處：把碩士學歷跟工作經驗的條件去掉
      search_page = requirement(1, args.key_word, '1', args.area, '', 'M',
                                args.min_salary, args.max_salary, '1', '',
                                '2018indexpoc', (page + 1))
      current_params = dict(search_page._asdict())

      content = fetch(current_params)
      data = content.json()
      # 修復處：Python跟C++ Java一樣 要件有異動都是要手動賦值一次的

      for row in data['data']['list']:
        for k in df_template.keys():
          df_template[k] = row[k]
          pass
        df_job = df_job._append([df_template], ignore_index=False)
        # 更新處：pandas 2.0.3不再支持append方法，這邊直接調用_append，不過可以的話用concat改寫更好
        pass
    df_job.to_csv('{}/{}/df_job.csv'.format(args.output_dir, current_time),
                  encoding="utf_8_sig")
    pass

  print("Mission complete.")
  pass


if __name__ == "__main__":
  run()
  pass
