str_number = input('1から10までの整数のどれかを入力してください')
sel_number = int(str_number)
while(sel_number<1 or sel_number > 10):
  print('入力した数字に誤りがあります')
  str_number = input('再度，入力してください')
  sel_number = int(str_number)
print('ありがとう．正しい数字です:',sel_number)
