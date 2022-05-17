count = 0
while (count < 4):
  try:
    str_number = input('整数を入力してください')
    sel_number = int(str_number)
    sel_number == str_number
    break
  except ValueError:
    print('正しくありません．再度，整数を入力してください')
    count = count + 1
print('ありがとう．チェックを終了します')
