# ########### 将 fre_list.txt 单词写入 myvocab.txt；myvocab.txt当作已知词汇列表################# 
# filename = "freq_list.txt"  # txt文件和当前脚本在同一目录下，所以不用写具体路径

# new_word_list=[]

# with open(filename, 'r') as file_to_read: # terminal 要调到当前目录
#     while True:
#         lines = file_to_read.readline()  # 整行读取数据
#         if not lines:
#             break
#         # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
#         line_words = [str(i) for i in lines.split()]
#         new_word_list.append(line_words[1])

# new_word_list=set(new_word_list)

# with open('myvocab.txt','a') as file_to_write:
#     for word in new_word_list:
#         file_to_write.writelines(word+"\n")

# print('书写结束')

############### part2: 以myvocab中的词汇为基础，统计字幕文件中出现的未见过的词汇和频数，并写入新的文件 new_word_output_list.txt"""""""""""

# params
work_dir="C:\\Users\\18813\\Desktop\\WordSmart.py\\"
file_with_known_words="myvocab.txt"
files_to_parse_list=["Felicity - 01x01 - Pilot.Unspecified.English.orig.Addic7ed.com.srt","Felicity - 01x02 - The last stand.Unspecified.English.orig.Addic7ed.com.srt"]
num_min_limit=0 

# procedure
known_word_set=set([',','.','!'])

with open(work_dir+file_with_known_words,'r',encoding='utf-8') as file_to_read:
    for line in file_to_read:
        line=line.strip()
        if (line=="") or (line[0]=='#'):
            continue 
        known_word_set.add(line.split()[0])

new_word_dict=dict()
num_list=[str(i) for i in range(0,10)]
for file_item in files_to_parse_list:
    with open(work_dir+file_item,'r',encoding='utf-8') as tmp_file:
        for line in tmp_file:
            line=line.strip()
            if (line=="") or (line[0] in num_list):
                continue

            tmp_word_list=line.split()
            for tmp_word in tmp_word_list:
                tmp_word=tmp_word.strip(',').strip('.').strip('!').strip('?').strip(':').strip('"').strip('-').strip('%').strip(',').strip('...')
                if ("'" in tmp_word) or ("ing" in tmp_word):
                    continue
                if tmp_word not in known_word_set:
                    tmp_word=tmp_word.lower()
                    if (tmp_word=="") or (False not in [i in num_list for i in tmp_word]):
                        continue
                    if tmp_word[-1]=='s':
                        if (tmp_word[0:-1] in known_word_set) or (tmp_word[0:-2] in known_word_set):
                            continue
                    if len(tmp_word)>3 and tmp_word[-3:]=="ies":
                        if tmp_word[0:-3]+"y" in known_word_set:
                            continue
                    if tmp_word[-2:]=="ed":
                        if (tmp_word[0:-1] in known_word_set) or (tmp_word[0:-2] in known_word_set) or (tmp_word[0:-3] in known_word_set):
                            continue
                    if tmp_word[-3:]=="ied":
                        if (tmp_word[0:-3]+"y" in known_word_set):
                            continue
                    if tmp_word[-2:]=="er":
                        if (tmp_word[0:-1] in known_word_set) or (tmp_word[0:-2] in known_word_set) or (tmp_word[0:-3] in known_word_set):
                            continue
                    if tmp_word[-3:]=="est":
                        if (tmp_word[0:-3] in known_word_set):
                            continue 
                    if len(tmp_word)>4 and tmp_word[-3:]=="iest":
                        if tmp_word[0:-4]+"y" in known_word_set:
                            continue
                    if len(tmp_word)>2 and tmp_word[0:2]=="un":
                        if tmp_word[3:] in known_word_set:
                            continue
                    if tmp_word[-2:]=="ly":
                        if (tmp_word[0:-2] in known_word_set) or (tmp_word[0:-3]+"y" in known_word_set):
                            continue
                    if tmp_word not in known_word_set:
                        if tmp_word not in new_word_dict:
                            new_word_dict[tmp_word]=1
                        else:
                            new_word_dict[tmp_word]=new_word_dict[tmp_word]+1

with open(work_dir+"output_list.txt",'w') as file_to_write:
    for key in new_word_dict:
        if new_word_dict[key]>num_min_limit:
            file_to_write.writelines(key+'\n')

print("结束过滤")

