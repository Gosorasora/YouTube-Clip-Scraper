# YouTube-Clip-Scraper
YouTube 동영상에서 가장 많이 재생된 구간을 자동으로 찾아서 클립으로 만들어주는 프로그램입니다.

## 🎯 이 프로그램이 하는 일
- YouTube 동영상의 "가장 많이 재생된 구간" 데이터를 분석
- 해당 구간들을 자동으로 추출하여 별도의 MP4 클립 파일로 저장
- 여러 동영상을 한 번에 처리 가능

## 📋 필요한 프로그램 설치

### 1. Python 설치 확인
터미널에서 다음 명령어로 Python이 설치되어 있는지 확인:
```bash
python --version
```
또는
```bash
python3 --version
```

### 2. 필요한 라이브러리 설치
터미널에서 다음 명령어들을 순서대로 실행:
```bash
pip install pytubefix moviepy requests
```

## 🚀 사용 방법

### 1단계: 프로젝트 다운로드
```bash
git clone https://github.com/wylieglover/YouTube-Clip-Scraper.git
cd YouTube-Clip-Scraper
```

### 2단계: 동영상 ID 설정
`create_clips.py` 파일을 텍스트 에디터로 열고, `main()` 함수 안의 `video_ids` 리스트에 원하는 YouTube 동영상 ID를 입력합니다.

**YouTube 동영상 ID 찾는 방법:**
- YouTube URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- 동영상 ID: `dQw4w9WgXcQ` (v= 뒤의 11자리 문자)

**코드 수정 예시:**
```python
video_ids = [
    "dQw4w9WgXcQ",    # 첫 번째 동영상
    "3iqIXEjTgcc",    # 두 번째 동영상  
    "abcd1234567",    # 세 번째 동영상
]
```

**중요한 점:**
- 따옴표 안에 ID만 입력하세요
- 여러 동영상을 처리하려면 쉼표로 구분해서 추가
- 현재 `"3iqIXEjTgcc"`가 예시로 들어있습니다

### 3단계: 프로그램 실행
```bash
python create_clips.py
```

## 📁 결과물 확인

프로그램이 완료되면 `clips` 폴더에 다음과 같은 파일들이 생성됩니다:

```
clips/
├── 동영상제목_clip_1.mp4
├── 동영상제목_clip_2.mp4
└── ...
```

**예시 결과:**
- `SCHD  , QQQ  _clip_1.mp4` - 첫 번째 인기 구간
- `SCHD  , QQQ  _clip_2.mp4` - 두 번째 인기 구간

## 🔧 프로그램 작동 과정

1. **동영상 다운로드**: YouTube에서 원본 동영상을 임시로 다운로드
2. **인기 구간 분석**: YouTube의 "가장 많이 재생된 구간" 데이터를 추출
3. **클립 생성**: 인기 구간만 잘라서 별도 파일로 저장
4. **정리**: 원본 동영상 파일은 자동으로 삭제

## ⚠️ 주의사항

- 인터넷 연결이 필요합니다
- 동영상 크기에 따라 처리 시간이 오래 걸릴 수 있습니다
- 일부 동영상은 "가장 많이 재생된 구간" 데이터가 없을 수 있습니다
- 저작권이 있는 콘텐츠는 개인적 용도로만 사용하세요

## 🐛 문제 해결

**"No module named 'pytubefix'" 오류가 나는 경우:**
```bash
pip install --upgrade pytubefix
```

**동영상 다운로드가 안 되는 경우:**
- 동영상 ID가 정확한지 확인
- 동영상이 비공개나 삭제되지 않았는지 확인

**클립이 생성되지 않는 경우:**
- 해당 동영상에 "가장 많이 재생된 구간" 데이터가 없을 수 있습니다
