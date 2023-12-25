# [PGS] 신규 아이디 추천 / IMP / 40
# 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
import re
def id_rec(new_id):
    # 1단계 : 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower() 
    # 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    chars_to_remove = '~!@#$%^&*()=+[{]}:?,<>/'
    translation_table = str.maketrans('', '', chars_to_remove)
    new_id = new_id.translate(translation_table)
    # 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)
    # 4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
    # 5단계 : 빈 문자열이라면, new_id에 "a"를 대입
    # 6-1단계 : 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 6-2단계 : 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    new_id = 'a' if len(new_id) == 0 else new_id[:15].strip('.')
    # 7단계 : 길이가 2자 이하라면, 마지막 문자를 new_id의 길이가 3이 될 때까지 반복
    if len(new_id) <= 2:
        while len(new_id)<3:
            new_id += new_id[-1]
    print(new_id)
        
    

id_rec(input('new_id:'))