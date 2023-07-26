# 用python batsearch.py進入則能做批量查詢
import subprocess
import time

commands = [
  "python 104-Crawler --key_word '後端工程師' --min_salary 35000 --area '6001001000'",
  "python 104-Crawler --key_word '後端工程師' --min_salary 35000 --area '6001002000'",
  "python 104-Crawler --key_word '軟體工程師' --min_salary 35000 --area '6001001000'",
  "python 104-Crawler --key_word '軟體工程師' --min_salary 35000 --area '6001002000'",
  "python 104-Crawler --key_word 'Java' --min_salary 35000 --area '6001001000'",
  "python 104-Crawler --key_word 'Java' --min_salary 35000 --area '6001002000'",
  "python 104-Crawler --key_word 'Django' --min_salary 35000 --area '6001001000'",
  "python 104-Crawler --key_word 'Django' --min_salary 35000 --area '6001002000'",
]

for command in commands:
  subprocess.run(command, shell=True)
  time.sleep(60)  # 為了避免太快執行完畢 時間還沒變 把檔案蓋掉；也減緩請求頻率
