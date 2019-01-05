FROM premsvmm/ducati:v1

RUN  mkdir -p /var/www/java
#  && chmod 777 /var/www/java -R
COPY . /var/www/java
WORKDIR /var/www/java
#CMD ["java", "mvn"]
#RUN apt-get install git-core
RUN mvn clean compile