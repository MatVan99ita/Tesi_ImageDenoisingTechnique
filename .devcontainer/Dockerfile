# Usa una versione di Ubuntu base
FROM ubuntu:20.04

# Impostazioni ambientali per evitare interattività durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Aggiorna il sistema e installa le dipendenze necessarie
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    wget \
    curl \
    perl \
    make \
    git \
    python3 \
    python3-pip \
    vim \
    unzip \
    bash \
    lsb-release \
    && apt-get clean

# Installa MiKTeX (versione base senza l'immagine miktex/miktex:ubuntu)
RUN wget -qO- https://miktex.org/download/ubuntu | bash && \
    miktexsetup --admin --update-fndb && \
    miktexsetup --admin --install

# Imposta MikTeX per il completamento automatico dei pacchetti
RUN initexmf --admin --set-config-value [MPM]AutoInstall=1 && \
    initexmf --admin --update-fndb

# Installa Pygments per il supporto a minted
RUN pip3 install Pygments

# Aggiungi i file di lavoro nel container
WORKDIR /workspace

# Lancia il container con bash
CMD ["bash"]
