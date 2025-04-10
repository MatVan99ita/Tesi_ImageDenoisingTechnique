FROM miktex/miktex:ubuntu

# Installa Python + Pygments
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    perl \
    make \
    git \
    curl \
    unzip \
    vim

# Installa pacchetti Python necessari per minted
RUN pip3 install Pygments

# Configura MiKTeX
RUN miktexsetup finish && \
    initexmf --admin --set-config-value [MPM]AutoInstall=1 && \
    initexmf --admin --update-fndb && \
    initexmf --update-fndb

WORKDIR /workspace
CMD ["bash"]
