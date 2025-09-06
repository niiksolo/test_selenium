FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl unzip wget gnupg2 \
    libnss3 libatk-bridge2.0-0 libxss1 libasound2 libx11-xcb1 \
    libxcomposite1 libxcursor1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
    chromium chromium-driver && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

ENV CHROME_BIN=/usr/bin/chromium

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /

CMD ["pytest", "tests", "--alluredir=allure-results", "-v", "-s"]