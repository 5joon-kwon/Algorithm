def solution(s):
    s = s.replace('{', '')
    s = s.replace('}','') 
    num_list = s.split(',') # 복잡한 문자열을 숫자만 들어있는 list로 바꿔줌
    
    s_set = set(num_list)   # 집합은 중복을 허락하지 않아 숫자의 종류를 파악하기 용이

    s_dic = {}              # 튜플의 원소 : 개수 를 dictionary로 표현
    for i in s_set:
        count = num_list.count(i)
        s_dic[i] = count
        
    s_dic = sorted(s_dic, key = lambda x : s_dic[x], reverse = True) # value 기준 정렬
    
    answer = list(map(int, s_dic))  # int 형태의 list로 변환
    
    return answer