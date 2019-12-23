FROM lambci/lambda:build-python3.6
ENV LANG C.UTF-8

WORKDIR /var/task
ADD . .

RUN rm -rf *.zip \
    && curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2017-03.zip > ./stable-headless-chromium-amazonlinux-2017-03.zip \
    && rm ./layers/python3-selenium-headless/headless/python/bin/headless-chromium \
    && unzip ./stable-headless-chromium-amazonlinux-2017-03.zip -d ./layers/python3-selenium-headless/headless/python/bin/

RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
  pip install -r requirements.txt -t /var/task

CMD zip -9yr deploy_package.zip . -x \*/__pycache__/\* \*.git/\* deploy_package.zip \*/tmp/\* venv/\* .DS_Store\* tmp\* .idea\*
