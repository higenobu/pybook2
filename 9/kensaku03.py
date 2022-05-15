def find_count(name,moji):
  i = 0
  count = 0
  while (i < len(name)):
    if name[i] == moji:
        count = count + 1
    i = i + 1
  return count
name = 'osakakyototokyojapan'
x = find_count(name,'a')
print(x)
