zaiko_dic = {'コップ': 10, '皿': 20, '茶碗': 10}
def inv_zaiko(zaiko_dic):
  inv_dic = dict()
  for k in zaiko_dic:
    w = zaiko_dic[k]
    if w not in inv_dic:
      inv_dic[w] = [k]
    else:
      inv_dic[w].append(k)
  return inv_dic
