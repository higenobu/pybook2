import time		# モジュールを読み込む
while (1):		# 全体をくり返す
  su = 'S'		# Sから始める
  for i in range(5):    # 5回くり返す
    su = su + 'u'	# 文字uを追加
    print(su)		# 表示
    time.sleep(1)	# 1秒休む
  ha = 'H'		# Hから始める
  for i in range(8):	# 8回くり返す
    ha = ha + 'a'	# 文字aを追加
    print(ha)		# 表示
    time.sleep(1)	# 1秒休む
