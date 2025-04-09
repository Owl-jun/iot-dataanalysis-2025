# iot-dataanalysis-2025
2025 IoT 개발자과정 빅데이터분석 리포지토리

## 1일차

### 머신러닝/딥러닝

<img src="./img/ml0001.png" width="750">
(출처 : NVIDIA)

- 인공지능(Artificial Intelligence: AI)의 분야
    - 컴퓨터가 사람의 행동을 흉내내는 모든 기술

- 머신러닝
    - 인공지능 하위 집합
    - 통계적 방법을 이용, 기계를 학습을 시키는 인공지능 기술

- 딥러닝
    - 머신러닝의 하위 집합
    - 신경망 기술을 이용, 머신러닝 기술 중 하나

- 인공지능 역사
    - 1943 - MCP뉴런
    - 1950 - 튜링(앨런 튜링) 테스트, 인공지능 테스트
    - 1957 - 퍼셉트론 이론
    - 1974 - 1차 AI겨울. 컴퓨터 성능 한계
    - 1980 - AI붐. 전문가 시스템(머신러닝)
    - 1987 - 2차 AI겨울. 전문가 시스템 실패
    - 2010 - 컴퓨팅 HW환경 비약적 발전. AI의 희망
    - 2015 - 텐서플로 발표
    - 2016 - 알파고

### 개박환경

#### 코랩
- Google Colaboratory, 2017년 발표
- 구글에서 만든 온라인 주피터노트북 개발 플랫폼
- 구글 드라이브 연동, 구글 서버 하드웨어 사용
    - 드라이브 ColabNotebooks 폴더에 저장
- 어디서나 파이썬 학습, 개발 등 가능
- https://colab.research.google.com/?hl=ko
- 런타임 유형
    - CPU, T4 GPU , v2-8 TPU - 무료
    - A100 GPU, L4 GPU, v5e-1 TPU - 유료
- 무료에서는 일정시간 넘게 사용시 세션이 끊어짐

#### VSCode
- 로컬 직접 환경 설정
- 사이킷런, 텐서플로, 쿠다, 파이토치 ...

##### 파이썬 가상환경
- 가상환경 생성 명령어
```shell
> python -m venv mlvenv
```
- 가상환경 사용
```shell
> mlvenv/Scripts/activate.ps1
```

- 가상환경은 깃허브에 올라가지 않도록 처리
- .gitignore에 /mlvenv 추가 후 깃허브 우선 푸쉬

- matplotlib 설치
```shell
> pip install matplotlib
```

- matplotlib 한글 설정
```python
from matplotlib import rcParams, font_manager, rc

font_path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name() # 실제 설치된 폰트 이름조회
rc('font', family=font) # 한글깨짐현상 해결!!
rcParams['axes.unicode_minus'] = False # 한글 사용시 마이너스 표시 깨짐 해결!
```

- scikitlearn 설치
```shell
> pip install scikit-learn
```

- tensorflow 설치
```shell
> pip install tensorflow==2.15.0
```

### 첫 번째 머신러닝
- 캐글 생선 데이터
    - https://www.kaggle.com/datasets/vipullrathod/fish-market
    
- 길이를 보고 도미(bream)인지 빙어(smelt)인지 판별
- 이진 분류(Binary Classification)
- [노트북](./DAY01/mldl01_도미빙어분류.ipynb)

### 지도 학습/ 비지도 학습
- 지도 학습 - 데이터 -> `입력`, 정답 -> `타겟` => 훈련 데이터(training data)
    - 정답이 있음.
    - 입력 -> 특성
    - 입력과 타겟을 모두 주어서 훈련을 시키는 것
- 비지도 학습 - 입력만 존재하고 타겟없이 훈련하는 것.
    - 알아서 패턴을 찾아보거라.
- 강화 학습 - 선택가능한 행동 중 당근과 채찍으로 최적의 행동양식 학습하는 것

#### 훈련 세트/테스트 세트
- `훈련` 세트 - 모델을 훈련시키기 위한 데이터
- `테스트` 세트 - 훈련 후 모델이 예측을 제대로 하는지 테스트하는 데이터

- 전체 데이터 7~80% 분리 후 훈련 세트로, 20~30%를 테스트 세트로 사용

#### 샘플링 편향
- 49개 데이터를 7:3으로 분리하면 
    - 34마리가 전부 도미가 훈련 세트
    - 1도미 + 14빙어로 테스트 세트

- 위 문제를 해결하기 위해서 데이터를 섞어준다.

#### 넘파이
- 수학 라이브러리의 일종. 파이썬에서 배열처리 쉽게 도와주기 위해 개발 됨.
- 2차원 배열이상 고차원 배열 조작 및 처리 간편한 도구.

- 시본(seaborn) 모듈(맷플롯립 하위 모듈) 설치
```shell
> pip install seaborn
```
- [노트북](./DAY01/mldl02_훈련%20테스트%20세트.ipynb)


## 2일차

### 빅데이터에 필요한 모듈
- Matplotlib(차트), Seaborn(차트꾸미기), Numpy(배열), Pandas(데이터 조작), Folium(지도), Faker(더미데이터 생성)

- [노트북](./DAY02/mldl01_주요모듈학습.ipynb)

### 데이터 전처리

### 선형회귀

### 로지스틱회귀

### 확률적 경사하강법

### 인공신경망

### 심층신경망

### 합성곱신경망

### 순차데이터와 순환신경망





## 8일차

### 코딩테스트