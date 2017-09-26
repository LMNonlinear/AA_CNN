import pandas as pd

df = pd.read_csv('labels.csv')

n_morethanone = 0
maximum=0
minumum=20
s=0
for index, row in df.iterrows():
    cnt=0

    tmp = row.tolist()[1:]
    for item in tmp:
        if item == 1:
            cnt += 1
    if cnt > 1:
        n_morethanone += 1
    if cnt > maximum:
        maximum=cnt
    if cnt < minumum:
        minumum = cnt

    s += cnt

print(n_morethanone)
print(maximum)
print(minumum)
print(float(s)/float(400))
