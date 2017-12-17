# Description

This is a tool which can search and download video from Youtube which use [youtube api](https://github.com/youtube/api-samples) and [youtube-dl](https://github.com/rg3/youtube-dl#description).

# Prerequisites

- Python 2.6 or greater
- The pip package management tool
- The Google APIs Client Library for Python:
  ```
  pip install --upgrade google-api-python-client
  ```
- The google-auth, google-auth-oauthlib, and google-auth-httplib2 for user authorization.
  ```
  pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
  ```
- Youtube-dl (On Linux, other platforms see more on [youtube-dl](https://github.com/rg3/youtube-dl#description) )
  ```
  sudo -H pip install --upgrade youtube-dl
  ```
- Create project on Google API console and get API key (enable Youtube Data API)

# Execution

1. Replace API key in youtubeapi.py Line10 ``` DEVELOPER_KEY = ...... ```
2. Run youtubeapi.py, and get $SearchKeyWord_id.txt
```
  python youtubeapi.py [OPTIONS]
  
  --q               search key word, default is baseball
  --max-results     max search result, default is 25
  --projection      360 or rectangular, default is 360
```
3. Run downlaodVideo.sh and get video
```
  sh downlaodVideo.sh $file(XXXX_id.txt) $dirDst
```

