## 토이프로젝트 
## 비밀번호 강도 분류기 학습시키기.

from sklearn.neighbors import KNeighborsClassifier  
import re
import numpy as np

kn = KNeighborsClassifier()

# 8자리 미만 = 0
# 조합X = 0
# 8자리 미만 , 영문 + 숫자 조합 = 1
# 8자리 이상 , 영문 , 숫자 조합 = 2
# 영문 + 숫자 + 8자리이상 + 특수문자 = 3

training_password = ['12','1234','qwer','qwerty','123456','12345678','qwertyui','qwwerreds','15334233412','1244214123','1234567',
                     '12qw','123qwe','432rew','134qrwe','qwer142',
                     '1424qrwe','123455qqwer','qwerr12345','1234qwasdf','123qwert',
                     'qwe123!@','qwer1234!@','qwert12345!@','qwert123!','qwasdf5342!']
training_target = [0] * 11 + [1] * 5 + [2] * 5 + [3] * 5

def dataTransformation(pwd) :
    length = len(pwd)
    has_digit = int(bool(re.search(r'\d',pwd)))
    has_letter = int(bool(re.search(r'[a-zA-Z]',pwd)))
    has_special = int(bool(re.search(r'[^a-zA-Z0-9]',pwd)))
    return [length,has_digit,has_letter,has_special]

training_input = [dataTransformation(pw) for pw in training_password]

input = np.array(training_input)
target = np.array(training_target)
np.random.seed(38)
index = np.arange(26)
np.random.shuffle(index)

kn.fit(input[index],target[index])
print("정확도 :") 
print(kn.score(input,target))

test_passwords = [
    '1234',         
    'password',     
    'pass123',      
    'pass1234',     
    'Pass123!',     
    'P@ssw0rd123!', 
    'abc',          
    'qwe123!@',     
    'asdfgh',       
    'abc1234567'    
]

# 전처리: 특징 추출
test_inputs = [dataTransformation(pw) for pw in test_passwords]

# 예측
predictions = kn.predict(test_inputs)

# 결과 출력
for pw, pred in zip(test_passwords, predictions):
    print(f"{pw:15} → 예측 강도: {pred}")


def checkPasswordSecurity(input) :
    pw = dataTransformation(input)
    return kn.predict([pw])[0]


print(checkPasswordSecurity('1234567'))

## 토이프로젝트 결과

## 트레이닝 셋이 적고, KNN 과 같이 거리기반의 경우 복잡한 조건 분류에 약하고, 정확도가 낮다.