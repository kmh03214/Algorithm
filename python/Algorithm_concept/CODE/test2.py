# 1. program으로 시작
def program_name(program,name):
    return True if name == program else False
# 2. 각 flag argument는 대응하는 flag의 flag_argument_type과 일치
def check_flag_arg(fg_rules,option,types):
    if fg_rules[option] == 'str':
        # [a-z][A-Z] 안에만 들어있어야 함.
        alphabet_dict = {i:1 for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        for s in types:
            if s not in alphabet_dict:
                return False
        return True
    elif fg_rules[option] == int:
        try:
            int(types)
            return True if fg_rules[option] == type(int(types)) else False
        except:
            return False
    else:
        return True if fg_rules[option] == types else False

# 3. 각 flag는 0번이나 1번 나타납니다.
# 4. flag_rules에 존재하는 flag만 나타납니다.

def solution(program, flag_rules, commands):
    fg_rules = {}
    answer = []
    
    for rule in flag_rules:
        r0,r1 = rule.split()
        if r1 == 'STRING': # string은 처리가 좀 필요할듯
            r1 = 'str'
        elif r1 == 'NUMBER':
            r1 = int
        else:
            r1 = None
        fg_rules[r0] = r1
    

    for command in commands:
        
        tmp_c = command.split()
        fg = 1
        for i in range(len(fg_rules)+1): # 총 flag_rules + program name까지 커맨드로 들어와야 함
            # 1번조건 체크 / 조건 틀리면 다음 커맨드 검사
            if i == 0:
                try:
                    name = tmp_c[i]
                except:
                    answer.append(False)
                    fg = 0
                    # print('Program name Error')
                    break

                if not program_name(program, name):
                    answer.append(False)
                    fg = 0
                    break
                else:
                    continue
                
            # 2번조건 체크
            try:
                option = tmp_c[(2*i)-1]
                if fg_rules[option] == None:
                    if 2*i >= len(tmp_c):
                        types = None
                        pass
                    elif tmp_c[2*(i)]:
                        answer.append(False)
                        fg = 0
                        break
                else:
                    types = tmp_c[2*(i)]
                    if option[0] != '-':
                        answer.append(False)
                        fg = 0
                        # print('Program flag_rules Error')
                        break
            except:
                answer.append(False)
                fg = 0
                #print('Program flag_rules Error')
                break
                
            if not check_flag_arg(fg_rules, option, types):
                answer.append(False)
                fg = 0
                break
            else:
                continue
        
        if fg:
            answer.append(True)
    
    return answer

solution('line',["-s STRING", "-n NUMBER", "-e NULL"],["line -n 100 -s hi -e", "lien -s Bye"])