# 특정 페이지에 접속 후 유지하는 목적의 코드입니다.

#### 전제조건 : 도커가 설치되어있어야함

#### 사용 예 :
    docker run --rm -it  \
        -e TARGET_URL='https://google.com' \
        -e WINDOW_MAX_COUNT=2 \
        -e TAB_MAX_COUNT_PER_WINDOW=10 \
        -e SLEEP_TIME_SEC=0.3 \
        kimjoin2/url-access-and-hold-on:latest
  
#### 환경변수 설명 :
    TARGET_URL : 접근하고 유지할 페이지의 url
    WINDOW_MAX_COUNT : 크로니움 브라우저의 최대 윈도우 갯수
    TAB_MAX_COUNT_PER_WINDOW : 각 윈도우마다의 탭 갯수
    SLEEP_TIME_SEC : 새 탭 혹은 창을 띄운 후 슬립타임(초단위, 소숫점 사용 가능)
    
#### 도커 허브 url : 
    https://hub.docker.com/repository/docker/kimjoin2/url-access-and-hold-on
