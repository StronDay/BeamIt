FROM python:3.11-slim

RUN pip install --upgrade pip 
COPY --from=openjdk:21-jdk-slim /usr/local/openjdk-21 /usr/local/openjdk-21
COPY --from=structurizr/lite /usr/local/structurizr-lite.war /usr/local/

ENV JAVA_HOME=/usr/local/openjdk-21
ENV LANG=C.UTF-8
ENV PATH=/usr/local/openjdk-21/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-21/bin/java 1  

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \ 
    wrk \
    iputils-ping \
    libpq-dev \
    libxtst6 \
    libxrender1 \
    libx11-6 \
    libxrandr2 \
    libxcomposite1 \
    libxdamage1 \
    libfontconfig1 \
    libfreetype6 \
    libxi6 \
    tree \
    postgresql \ 
    postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

COPY . .
COPY ./.devcontainer/extensions/bee-c4-dsl-extension.vsix /tmp/

COPY ./services/api/requirements.txt /tmp/api/requirements.txt
COPY ./services/auth_service/requirements.txt /tmp/auth_service/requirements.txt
COPY ./services/cipher_service/requirements.txt /tmp/cipher_service/requirements.txt
COPY ./services/user_service/requirements.txt /tmp/user_service/requirements.txt

# RUN pip install --no-cache-dir -r /tmp/api/requirements.txt
# RUN pip install --no-cache-dir -r /tmp/user_service/requirements.txt

RUN pip install --no-cache-dir \
    -r /tmp/api/requirements.txt \
    -r /tmp/auth_service/requirements.txt \
    -r /tmp/cipher_service/requirements.txt \
    -r /tmp/user_service/requirements.txt

RUN apt-get update && apt-get install -y zsh git curl
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN chsh -s $(which zsh)
CMD ["zsh"]

ENTRYPOINT ["/bin/sh", "-c" ,"java -jar /usr/local/structurizr-lite.war /workspace/structurizr"]