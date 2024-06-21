FROM docker.io/library/ubuntu:latest

RUN apt update && apt full-upgrade -y
RUN apt install python3-full -y
RUN apt install python3-pip -y
RUN pip3 install mythic-container --break-system-packages

RUN apt install mingw-w64 -y

WORKDIR /Mythic/

CMD ["python3", "main.py"]