2023년 여름방학동안 동아대학교에서 진행된 인공지능 빅데이터 실무교육을 이수하고 만들어본 프로젝트입니다.
# 주제
교육시간에 사용했던 예제를 이용해 강화학습 알고리즘의 성능을 비교해보는 것이 주제입니다.
## Installation
### Gymnasium
To install the base Gymnasium library, use ```pip install gymnasium```
### stable-baselines3
Install the Stable Baselines3 package:
```pip install stable-baselines3[extra]```
## lunar_lander.py 설명
우주선을 목표한 지점에 정확하게 착륙시킬 수 있도록 강화학습을 시키고 그 결과를 출력하는 코드입니다.  
dqn_lunar.zip 과 ppo_lunar.zip에 학습시킨 데이터들이 저장되어있고 그 파일을 load해서 화면에 출력합니다.  
직접 학습을 시켜보고 싶다면 주석처리한 부분을 취소하고 원하는 알고리즘을 import해준 뒤 적용해서 코드를 돌려보시기 바랍니다.
