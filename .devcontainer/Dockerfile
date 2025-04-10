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

# Installa Pygments per il supporto a minted
RUN pip3 install Pygments

# Impostazione della variabile d'ambiente per Strawberry Perl
ENV PATH="/strawberry-perl/bin:${PATH}"

# Impostazione della variabile d'ambiente per MiKTeX
ENV PATH="/miktex/bin/x64:${PATH}"

# Aggiungi i file di lavoro nel container
WORKDIR /workspace

# Comando di avvio
CMD ["bash"]
