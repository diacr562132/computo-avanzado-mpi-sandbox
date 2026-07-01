FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openmpi-bin \
    libopenmpi-dev \
    openssh-server \
    iputils-ping \
    build-essential \
    nano \
    procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir mpi4py numpy matplotlib

RUN mkdir -p /var/run/sshd /root/.ssh

RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -N "" \
    && cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys \
    && chmod 700 /root/.ssh \
    && chmod 600 /root/.ssh/authorized_keys

RUN printf "Host *\n    StrictHostKeyChecking no\n    UserKnownHostsFile=/dev/null\n" > /root/.ssh/config

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

WORKDIR /workspace

CMD ["/usr/sbin/sshd", "-D"]
