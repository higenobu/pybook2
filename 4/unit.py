wtype = input('変換のタイプは？')
var1 = input('数字を入力してください')
float_var1 = float(var1)
if (wtype == 'p-k'):
  result = float_var1 * 0.45359293319936
if (wtype == 'f-m'):
  result = float_var1 * 0.3048
print(result)
