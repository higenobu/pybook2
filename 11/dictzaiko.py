zaiko_dic = {'コップ': 10, '皿': 20, '茶碗': 10}
def find_zaiko_dic(product,zaiko_dic):
  if product in zaiko_dic:
    return zaiko_dic[product]
