memo = u'今日は山田さんと田中さんと松永さんが私の家（松尾）にやってきてBQパーティーをしました'
kaisu = 0
kaisu_b = 0
for x in memo:
  if x == u'松':
      kaisu += 1
      continue
  if x == u'B':
    kaisu_b += 1
    continue
print('松の回数' + str(kaisu))
print('Bの回数' + str(kaisu_b))
