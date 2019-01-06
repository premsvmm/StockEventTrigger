FROM premsvmm/sherlock

RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8
RUN  mkdir -p /var/www/premsvmm

COPY . /var/www/premsvmm
WORKDIR /var/www/premsvmm

