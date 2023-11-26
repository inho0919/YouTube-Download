# YouTube-Download API

Pytube 응용

YouTube 음원추출, 영상추출, 플레이리스트 추출 API

### 1. Requirements
```
* OS : Windows 10, Ubuntu, Cent OS
* Python : 3.10.11 이상
* pip : 23.1.2
* pytube : 15.0.0
```

### 2. Install

* pip 설치

```pip install pytube```

* Git 다운로드

```git clone https://github.com/inho0919/YouTube-Download.git```

### 3. Use
 - Include
   
   ```python
   
   from API.YouTube import YouTube

   ```

 
 - Single Music Download

  ```python

  # YouTube URL
  singleMusicURL = "[YOUTUBE_URL]"

  # Windows : \\, Linux : /
  singleMusicPath = "[YOUR_PATH]" 

  # Execute
  singleMusicDownload = YouTube.singleMusic(singleMusicURL, singleMusicPath)

  # Show Result
  print(singleMusicDownload)

  ```


 - Single Video Download

 ```python

  # YouTube URL
  singleVideoURL = "[YOUTUBE_URL]"

  # Windows : \\, Linux : /
  singleVideoPath = "[YOUR_PATH]" 

  # Execute
  singleVideoDownload = YouTube.singleVideo(singleVideoURL, singleVideoPath)

  # Show Result
  print(singleVideoDownload)

 ```


 - Multi Music Download

 ```python

  # YouTube URL List
  multiMusicURL = [
      "[YOUTUBE_URL_1]",
      "[YOUTUBE_URL_2]",
      "[YOUTUBE_URL_3]",
      ...
  ]

  # Windows : \\, Linux : /
  multiMusicPath = "[YOUR_PATH]"

  # Execute
  multiMusicDownload = YouTube.multiMusic(multiMusicURL, multiMusicPath)

  # Show Result
  print(multiMusicDownload)

 ```


 - Multi Video Download

 ```python

  # YouTube URL List
  multiVideoURL = [
      "[YOUTUBE_URL_1]",
      "[YOUTUBE_URL_2]",
      "[YOUTUBE_URL_3]",
      ...
  ]

  # Windows : \\, Linux : /
  multiVideoPath = "[YOUR_PATH]"

  # Execute
  multiVideoDownload = YouTube.multiVideo(multiVideoURL, multiVideoPath)

  # Show Result
  print(multiVideoDownload)

 ```


 - Playlist Music Download

 ```python

  # YouTube Playlist URL
  playlistMusicURL = "[YOUTUBE_URL]"

  # Windows : \\, Linux : /
  playlistMusicPath = "[YOUR_PATH]"

  # Execute
  playlistMusicDownload = YouTube.playlistMusic(playlistMusicURL, playlistMusicPath)

  # Show Result
  print(playlistMusicDownload)

 ```


 - Playlist Video Download

 ```python

  # YouTube Playlist URL
  playlistVideoURL = "[YOUTUBE_URL]"

  # Windows : \\, Linux : /
  playlistVideoPath = "[YOUR_PATH]"

  # Execute
  playlistVideoDownload = YouTube.playlistVideo(playlistVideoURL, playlistVideoPath)

  # Show Result
  print(playlistVideoDownload)

 ```

### 4. Caution

다운로드 되지 않은 경우는 다음과 같습니다.

* 잘못된 URL
* 연령 제한이 걸려있는 경우
* 비공개 동영상
* 멤버십 전용 동영상


PS. ~~사실 그냥 Pytube 써도 되는데 그거마저 귀찮은 사람들을 위해 제작. 아무도 안쓰면 내가 씀~~
