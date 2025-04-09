## TOYPROJECT . 넘파이 및 사이킷런 튜토리얼 겸 비밀번호 강도체크 학습시켜보기

import re
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

"""
조합 : 대문자, 소문자, 숫자, 특문
0점(취약) : 8자 미만 || 조합X (조합 2개미만)
1점(보통) : 8자 이상 && 조합O (조합이 2~3개)
2점(높음) : 8자 이상 && 조합O (모든 조합)
"""

def check(pw):
    length = len(pw)
    has_num = int(bool(re.search(r'[0-9]', pw)))
    has_upper = int(bool(re.search(r'[A-Z]', pw)))
    has_lower = int(bool(re.search(r'[a-z]', pw)))
    has_special = int(bool(re.search(r'[^a-zA-Z0-9]', pw)))
    return [length, has_num, has_upper, has_lower, has_special]

# 학습용 데이터셋
x_train = ['1q2w!#','7654321','765rewq','1q2w3e4','abcdefg','9384726375','asdpfqoiweki','ASSDGDFEWFE','ASDFD','#!$#$',
           '!#$@#%!$^!^$#','popopo','Po1@','Pp#221','power','wdk6666','lhw3333','ksj','3333','@#AS',
           '1q2w3e4r', '1234qwer','ASVD12432','Abasd124534','poqwe1423','!@#QWERTE','QRWE1234','qweQWE123', 'POPO)(@#)123', '1234qweRE',
           'ABC!@#$as', 'asdQWE123', 'PpP#@QWE', 'poqwe(*&^)', '!@$#POIUasdf', 'a@s!p$s@p%', '124214qwerr', '142!@$#qwre', ' #$@qpwoQWR', 'QWR1243!@$',
           'Tlqkfdk12!@', 'Ehdrhks12!@','!@987Dlguddn', 'Chlqhwjd!@!233', 'ghkdTjrwns12%$', '!1qQ2@wW3#eR', '!@#qweQWE12', 'jameSp$2p!!q9', 'ipV4#21PP', 'qwpo12!@$WOI',
           'Qkrrhksgh1**', 'dksTjdwn16%3', 'Tjdaudrjs&^12', 'ChatGpT3!@R', 'KFDIII12qwe$#' , '#%@14Oiwo34', 'q!23r$rTP389', 'P#O1a5s#189', '!w33Q2sije', '!q@w3R2Ss1*ki']
y_target = [0] * 20 + [1] * 20 + [2] * 20

# numpy 배열로 변환
X_train = np.array([check(data) for data in x_train])
y_target = np.array(y_target)

# 섞기
np.random.seed(42)
index = np.arange(60)
np.random.shuffle(index)

# 학습
kn = KNeighborsClassifier()
kn.fit(X_train[index], y_target[index])


while True :
    print("비밀번호 입력 : " , end = '')
    inStr = input()
    pw = check(inStr)
    answer = kn.predict([pw,])[0]

    if answer==0 :
        print('비밀번호 강도 : 취약')
    elif answer==1 :
        print('비밀번호 강도 : 보통')
    elif answer==2 :
        print('비밀번호 강도 : 강력')
    else : print('에라 에라 에라')


## 정확도를 어떻게 하면 올릴 수 있을까
## 라이브러리 사용법을 학습하는데 치중하여 프로젝트를 완성해보았다.
## 생각해보니 굳이 안써도 될거 같다. (if 문으로 더 정확하게 구현가능 할 듯)