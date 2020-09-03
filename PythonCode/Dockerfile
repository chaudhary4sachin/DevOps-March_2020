#publicly available docker image "python" on docker hub will be pulled

FROM python
FROM qnib/pytest
#FROM seleniumstandalonechrome

#creating directory calculator in container (linux machine)
RUN mkdir c:\home\seldock

#copying calculator.py from local directory to container's selenium folder

COPY seldocktest.py /home/seldock/seldocktest.py
COPY selenium-server-standalone-3.141.59.jar /home/seldock/selenium-server-standalone-3.141.59.jar

#running calculator.py in container
#CMD pytest /home/seldock/seldocktest.py