# [Dies ist eine Datei, die ein Beispiel fuer die Dateiaufrufmethode darstellt]
# API.YouTube-Bibliothek importieren
from API.YouTube import YouTube



# 1. Single Music Download ===================
# YouTube URL
singleMusicURL = "[YOUTUBE_URL]"
# Windows : \\, Linux : /
singleMusicPath = "[YOUR_PATH]" 
# Execute
singleMusicDownload = YouTube.singleMusic(singleMusicURL, singleMusicPath)
# Show Result
print(singleMusicDownload)



# 2. Single Video Download ===================
# YouTube URL
singleVideoURL = "[YOUTUBE_URL]"
# Windows : \\, Linux : /
singleVideoPath = "[YOUR_PATH]" 
# Execute
singleVideoDownload = YouTube.singleVideo(singleVideoURL, singleVideoPath)
# Show Result
print(singleVideoDownload)



# 3. Multi Music Download ===================
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



# 4. Multi Video Download ===================
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



# 5. Playlist Music Download ===================
# YouTube Playlist URL
playlistMusicURL = "[YOUTUBE_URL]"
# Windows : \\, Linux : /
playlistMusicPath = "[YOUR_PATH]"
# Execute
playlistMusicDownload = YouTube.playlistMusic(playlistMusicURL, playlistMusicPath)
# Show Result
print(playlistMusicDownload)



# 6. Playlist Video Download ===================
# YouTube Playlist URL
playlistVideoURL = "[YOUTUBE_URL]"
# Windows : \\, Linux : /
playlistVideoPath = "[YOUR_PATH]"
# Execute
playlistVideoDownload = YouTube.playlistVideo(playlistVideoURL, playlistVideoPath)
# Show Result
print(playlistVideoDownload)