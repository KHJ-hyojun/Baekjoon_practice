word = input().upper()
w_list = list(set(word))
cnt_list = []

for i in w_list:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(w_list[cnt_list.index(max(cnt_list))])


