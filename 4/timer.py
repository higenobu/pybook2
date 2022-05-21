import time
timer = input('秒単位の時間を入力してください')
int_timer = int(timer)
add_timer = int_timer+10
time.sleep(add_timer)
print('タイマーの時間に10秒を足した時間が経過しました')
