import pytest
from load_scores import load_scores


# 정상 ①: 정상 파일 읽기
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5
    assert len(skipped) == 5


# 정상 ②: 빈 줄 건너뛰기
def test_빈_줄은_건너뛴다(tmp_path):
    path = tmp_path / "blank.csv"
    path.write_text(
        "name,score\n김철수,90\n\n이영희,80\n",
        encoding="utf-8-sig"
    )

    kept, skipped = load_scores(path)

    assert kept == [("김철수", 90), ("이영희", 80)]
    assert skipped == []


# 정상 ③: 이름에 쉼표가 있는 경우
def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert ("최,네번", 77) in kept


# 예외 ①: 존재하지 않는 파일
def test_없는_파일이면_오류가_난다(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "없는파일.csv")


# 예외 ②: 헤더만 있는 파일
def test_헤더만_있으면_빈_결과():
    assert load_scores("empty.csv") == ([], [])


# 경계값 테스트
@pytest.mark.parametrize("score, valid", [
    (-1, False),
    (0, True),
    (1, True),
    (99, True),
    (100, True),
    (101, False),
])
def test_점수_경계값(tmp_path, score, valid):
    path = tmp_path / "boundary.csv"
    path.write_text(
        f"name,score\n김철수,{score}\n",
        encoding="utf-8-sig"
    )

    kept, skipped = load_scores(path)

    if valid:
        assert kept == [("김철수", score)]
        assert skipped == []
    else:
        assert kept == []
        assert skipped == [
            (2, f"김철수,{score}", "점수가 0~100 밖")
        ]

# 점수가 비어 있는 경우
def test_점수가_비어_있으면_건너뛴다(tmp_path):
    path = tmp_path / "blank_score.csv"
    path.write_text(
        "name,score\n김철수,\n",
        encoding="utf-8-sig"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert skipped == [
        (2, "김철수,", "점수가 비어 있음")
    ]


# 프로그램 직접 실행 및 출력 확인
def test_프로그램을_직접_실행한다(monkeypatch, capsys):
    import runpy
    import sys

    monkeypatch.setattr(
        sys, "argv", ["load_scores.py", "scores.csv"]
    )

    runpy.run_path("load_scores.py", run_name="__main__")

    output = capsys.readouterr().out

    assert "읽은 줄 : 5개" in output
    assert "건너뛴 줄 : 5개" in output

def test_이름이_비어_있으면_건너뛴다(tmp_path):
    path = tmp_path / "blank_name.csv"
    path.write_text(
        "name,score\n,90\n",
        encoding="utf-8-sig"
    )

    kept, skipped = load_scores(path)

    assert kept == []
    assert skipped == [
        (2, ",90", "이름이 비어 있음")
    ]