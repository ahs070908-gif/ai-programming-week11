# 성적 관리 프로그램

## 1. 무엇을 하나요? (What)
성적 CSV 파일을 읽어 유효한 이름과 점수를 반환하고,
유효하지 않은 데이터는 건너뛴 이유와 함께 기록하는 프로그램입니다.

## 2. 왜 만들었나요? (Why)
성적 데이터를 받고 그 데이터를 바탕으로 원하는 정보를 불러낼 때, 전용 프로그램이 없어서 불편함을 느낄 수 있기 때문이다.

## 3. 어떻게 쓰나요? (How)

설치 명령어:
python -m pip install pytest pytest-cov

실행 명령어:
python load_scores.py

## 4. 어떻게 테스트하나요?

테스트 실행:
python -m pytest test_load_scores.py

커버리지 측정:
python -m pytest test_load_scores.py --cov=load_scores --cov-report=term-missing

테스트 결과:
- 전체 테스트: 14개
- 통과: 14개
- 실패: 0개
- 커버리지: 100%

## 5. 파일 구성

- load_scores.py: 성적 CSV를 읽고 검증하는 프로그램
- test_load_scores.py: 정상, 예외, 경계값 등을 검증하는 테스트
- test_ai_A.py: 코드를 제공하여 AI가 생성한 테스트
- test_ai_B.py: 명세서를 제공하여 AI가 생성한 테스트
- scores.csv: 성적 테스트용 데이터
- empty.csv: 헤더만 있는 테스트용 파일
- bug3_logic.py: 논리 오류 확인용 프로그램
- README.md: 프로그램 설명 및 사용 방법

## 6. 만든 사람

- 이름: 안효석
- 학번: 2026100138
- AI 활용: 테스트 코드 작성, 오류 분석, 커버리지 분석 및 GitHub 사용 방법에 ChatGPT를 활용하였습니다.
