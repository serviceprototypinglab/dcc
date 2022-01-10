FROM ubuntu:18.04

RUN apt-get update && apt-get install -y openssh-client git python3 python3-pip python3-setuptools

RUN useradd -m user
RUN mkdir -p /home/user/.ssh

COPY collect.py consensus.py requirements.txt verify.py env.sh /home/user/
WORKDIR /home/user/
RUN pip3 install -r requirements.txt

RUN chown -R user:user /home/user/.ssh
USER user

ENTRYPOINT ["sh", "env.sh"]
