while(True):
  try:
    str_number = input('整数を入力してください')
    sel_number = int(str_number)
    sel_number == str_number
    break
  except ValueError:
    print('正しくありません．再度，整数を入力してください')

print('ありがとう．正しい数字です:',sel_number)

