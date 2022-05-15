def e_counter(s):
  wd = dict()
  for a in s:
    if a not in wd:
      wd[a] = 1
    else:
      wd[a] += 1
  return wd				
rr = e_counter('takeyabuyaketa')
print(rr)