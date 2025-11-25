text="apple banana apple orange banana apple"
dict_counter = {}
for  i in text.split():               # or      for i in text.split():
    if i not in dict_counter:         #            dict_counter[i]=dict_counter.get(i,0)+1
        dict_counter[i]=0             #         print(dict_counter)
    dict_counter[i]+=1
print(dict_counter)        

scores=[("tom",80),("jerry",90),("mike",85),("tom",95)]
total_score={}
for name,score in scores:
    if name not in total_score:
        total_score[name]=0
    total_score[name]+=score
print(total_score)

participants=["tom","jerry","mike","tom","jerry","tom"]
participation_count={}
for name in participants:
    if name not in participation_count:
        participation_count[name]=0
    participation_count[name]+=1
print(participation_count)    
