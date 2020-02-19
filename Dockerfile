FROM alpine:3.11

RUN apk add python3 chromium chromium-chromedriver
RUN pip3 install selenium

COPY test.py /
COPY run.sh /

RUN chmod +x /run.sh

ENTRYPOINT /run.sh
