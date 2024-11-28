FROM ubuntu:latest
LABEL authors="julien"

ENTRYPOINT ["top", "-b"]