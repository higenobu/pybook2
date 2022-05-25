def find_string(name,moji):
  i = 0
  while (i < len(name)):
    if name[i] == moji:
      return i
    i = i + 1
  return -1
