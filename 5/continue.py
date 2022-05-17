while (True):
  str_number = input('整数を入力してください')
  sel_number = int(str_number)
  if sel_number == 5:
    print('5は嫌いです．違う整数を入力してください')
    continue
  print('ありがとう．この数字は整数です：',sel_number)
  break
