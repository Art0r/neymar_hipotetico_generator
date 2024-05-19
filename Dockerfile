FROM python:3.10-slim  AS builder

WORKDIR /app/neymar_hipotetico

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y binutils 

RUN pip install --no-cache-dir -r requirements.txt

RUN pyinstaller --onefile --add-data "prompt.txt:." main.py

FROM debian:latest

WORKDIR /app/neymar_hipotetico

RUN apt-get update && apt-get install -y gnupg gnupg2 gnupg1 wget

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update && apt-get install -y google-chrome-stable

COPY --from=builder /app/neymar_hipotetico/dist/main .
COPY --from=builder /app/neymar_hipotetico/prompt.txt .
COPY --from=builder /app/neymar_hipotetico/.env .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD [ "./main" ]