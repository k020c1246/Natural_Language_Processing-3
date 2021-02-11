
#ファイルの読み込み
f = open('neko1.txt')
data = f.read()
#print(data)

#形態素解析
tg = MeCab.Tagger("-Ochasen")
output=tg.parse(data)
#print(output)

#1行単位に分割
list_a=output.split("\n")

#あとで使うリストを定義
list0=[]
list1=[]
list2=[]
list3=[]

#全行をループ
for i in range(len(list_a)):

  #タブで分割
  list_buf=list_a[i].split("\t")

  #形態素解析が正確にできているかどうかを要素数で判定
  if len(list_buf) > 3:

    #各要素をリストに追加
    list0.append(list_buf[0])
    list1.append(list_buf[1])
    list2.append(list_buf[2])
    list3.append(list_buf[3])

for i in range(len(list1)-2):
  if str(list3[i]).find("名詞")>-1 and str(list0[i+1])=="の" and str(list3[i+2]).find("名詞")>-1:
    print(str(list0[i])+str(list0[i+1]+str(list0[i+2])))