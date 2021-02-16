info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150","- and - and - and - 140","- and - and - and - 130"]

# def make_bit_table(info):
#     lang = {'python':'', 'cpp':'', 'java':'', '-':''}
#     position = {'frontend':'', 'backend':'', '-':''}
#     exp = {'junior':'', 'senior':'', '-':''}
#     food = {'chicken':'', 'pizza':'', '-':''}
#     score = []

#     for i in range(len(info)):
#         info_tmp = info[i].split()
#         score.append(int(info_tmp[4]))
#         lang['-'] += '1'
#         if info_tmp[0] == 'python':
#             lang['python'] += '1'
#             lang['cpp'] += '0'
#             lang['java'] += '0'
#         elif info_tmp[0] == 'cpp':
#             lang['python'] += '0'
#             lang['cpp'] += '1'
#             lang['java'] += '0'
#         else: # java
#             lang['python'] += '0'
#             lang['cpp'] += '0'
#             lang['java'] += '1'
        
#         position['-'] += '1'
#         if info_tmp[1] == 'frontend':
#             position['frontend'] += '1'
#             position['backend'] += '0'
            
#         else: # backend
#             position['frontend'] += '0'
#             position['backend'] += '1'

#         exp['-'] += '1'
#         if info_tmp[2] == 'junior':
#             exp['junior'] += '1'
#             exp['senior'] += '0'
#         else:
#             exp['junior'] += '0'
#             exp['senior'] += '1'
        
#         food['-'] += '1'
#         if info_tmp[3] == 'chicken':
#             food['chicken'] += '1'
#             food['pizza'] += '0'
#         else:
#             food['chicken'] += '0'
#             food['pizza'] += '1'

#     return lang, position, exp, food, score

# def bit_and_oper(str1,str2,str3,str4):
#     ret = []
#     for i in range(len(str1)):
#         if int(str1[i]) & int(str2[i]) & int(str3[i]) & int(str4[i]) == 1:
#             ret.append(i)
#     return ret

# def solution(info, query):
#     answer = []
#     lang,position,exp,food,score = make_bit_table(info)
#     memory = {}
    
#     for q in query:

#         q_tmp = q.split()
#         q_lang,q_pos,q_exp,q_food,q_score = q_tmp[0],q_tmp[2],q_tmp[4],q_tmp[6],q_tmp[7]

#         combi = q_lang[0] + q_pos[0] + q_exp[0] + q_food[0]

#         if combi not in memory:
#             con = bit_and_oper(lang[q_lang], position[q_pos], exp[q_exp], food[q_food])
#             memory[combi] = con
#         else:
#             con = memory[combi]
#             print("memory")

#         cnt = 0
#         for i in range(len(con)):
#             if score[con[i]] >= int(q_score):
#                 cnt+=1
#         answer.append(cnt)

#     return answer

# import itertools
# import bisect

# def solution(info, query):
    
#     lang_map = {'python':'0' ,'cpp':'1' ,'java':'2', '-':'3'}
#     pos_map = {'backend':'0' ,'frontend':'1' ,'-':'3'}
#     exp_map = {'junior':'0' ,'senior':'1' ,'-':'3'}
#     food_map = {'chicken':'0' ,'pizza':'1' ,'-':'3'}
#     def make_table(info):
#         info_table = {}

#         for i in info:
#             lang,pos,exp,food,score = i.split()
#             score = int(score)
#             for a in (lang_map[lang],'3'):
#                 for b in (pos_map[pos], '3'):
#                     for c in (exp_map[exp],'3'):
#                         for d in (food_map[food],'3'):
#                             tmp_info = a+b+c+d
#                             if tmp_info not in info_table:
#                                 info_table[tmp_info] = [score]
#                             else:
#                                 info_table[tmp_info].append(score)

#             # for product in itertools.product((lang_map[lang],'3'), (pos_map[pos], '3') , (exp_map[exp],'3') , (food_map[food],'3')):
#             #     tmp_info = ''.join(product)
#             #     if tmp_info not in info_table:
#             #         info_table[tmp_info] = [score]
#             #     else:
#             #         info_table[tmp_info].append(score)
#         return info_table

#     answer = []
#     info_table = make_table(info)
#     for q in query:

#         q_tmp = q.split()
#         q_lang,q_pos,q_exp,q_food,q_score = lang_map[q_tmp[0]],pos_map[q_tmp[2]],exp_map[q_tmp[4]],food_map[q_tmp[6]],q_tmp[7]
#         q_score = int(q_score)
#         combi = q_lang + q_pos + q_exp + q_food

#         for inf in info_table:
#             info_table[inf].sort()

#         if combi in info_table:
#             filtering_scores = info_table[combi]
#             idx = bisect.bisect_left(filtering_scores,q_score)
#             print(filtering_scores,idx)
#             answer.append(len(filtering_scores) - idx)
#         else:
#             answer.append(0)
            
#     return answer

# print(solution(info,query))





import itertools
import bisect

def solution(info, query):

    def make_table(info):
        info_table = {}

        for i in info:
            lang,pos,exp,food,score = i.split()
            score = int(score)
            for a in (lang,'-'):
                for b in (pos, '-'):
                    for c in (exp,'-'):
                        for d in (food,'-'):
                            tmp_info = a+b+c+d
                            if tmp_info not in info_table:
                                info_table[tmp_info] = [score]
                            else:
                                info_table[tmp_info].append(score)

            # for product in itertools.product((lang_map[lang],'3'), (pos_map[pos], '3') , (exp_map[exp],'3') , (food_map[food],'3')):
            #     tmp_info = ''.join(product)
            #     if tmp_info not in info_table:
            #         info_table[tmp_info] = [score]
            #     else:
            #         info_table[tmp_info].append(score)
        return info_table

    answer = []
    info_table = make_table(info)
    for q in query:

        q_tmp = q.split()
        q_lang,q_pos,q_exp,q_food,q_score = q_tmp[0], q_tmp[2], q_tmp[4], q_tmp[6], q_tmp[7]
        q_score = int(q_score)
        combi = q_lang + q_pos + q_exp + q_food

        for inf in info_table:
            info_table[inf].sort()

        if combi in info_table:
            filtering_scores = info_table[combi]
            idx = bisect.bisect_left(filtering_scores,q_score)
            print(filtering_scores,idx)
            answer.append(len(filtering_scores) - idx)
        else:
            answer.append(0)
            
    return answer

print(solution(info,query))




