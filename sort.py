
file = "all.txt"

uniqlines = set(open(file,'r', encoding='utf-8').readlines())
gotovo = open(file,'w', encoding='utf-8').writelines(set(uniqlines))
 