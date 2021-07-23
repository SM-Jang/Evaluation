# Evaluation


1) Edit Score
string distance(Edit distance)
Levenshtein 과 같이 string 을 이용하여 정의
string 을 변화하기 위한 edit 방법을 세 가지로 분류합니다.
 1. delete: ‘점심을먹자 → 점심먹자’ 로 바꾸기 위해서는 '을' 삭제해야 합니다.
 2. insert: ‘점심먹자 → 점심을먹자’ 로 바꾸기 위해서는 '을' 삽입해야 합니다.
 3. substitution: ‘점심먹자 → 점심먹장’ 로 바꾸기 위해서는 '자'를 '장'으로 치환해야 합니다.


2) Classification Score
Sci-kit learn package
- confusion matrix
- precision
- recall
- accuracy
- f1_score