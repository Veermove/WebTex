FROM ubuntu

WORKDIR /WebTex

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository universe
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get -y install texlive-xetex
RUN apt-get -y install texlive-fonts-recommended
RUN apt-get -y install texlive-fonts-extra
RUN apt-get -y install pip
RUN apt-get -y install python3
RUN pip install flask


COPY . . 
ENV PORT=8080
EXPOSE 8080
CMD python3 app.py
