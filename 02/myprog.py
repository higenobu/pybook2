def substr(data,s,l): #関数名とそのパラメータの指定
  if len(data) > 0: 
  #dataという名前の変数の中に入っている値の長さ > 0の判定
    if s < len(data):
      if l < len(data):
        result = data[s:l]
        #開始の位置から終指定の位置までのdataをresultに入れる
      else:
        result = data[s:]
        #開始の位置から終指定の位置までのdataをresultに入れる	
    else:
      print('s is too big')
      #開始の位置がdataの長さの外にある
      result = -1
  else:
    print('string is null') #Dataはない
    result = -1
  return result #結果を返す
