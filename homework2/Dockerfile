FROM ubuntu:20.04

WORKDIR /work
COPY . /work

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    texlive-latex-extra



# Устанавливаем зависимости Python из файла requirements.txt
RUN python3 -m pip install -r requirements.txt

# Запускаем скрипт Python для генерации LaTeX файла, а затем компилируем его в PDF
CMD python3 2-3.py && pdflatex main.tex