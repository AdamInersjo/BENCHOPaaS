FROM fedora:30

RUN dnf update
RUN adduser -m fedora -s /bin/bash 
RUN dnf install -y python3-pip octave
RUN mkdir -p /home/fedora/BENCHOP
COPY . /home/fedora/BENCHOP/
WORKDIR /home/fedora/BENCHOP
RUN pip3 install flask oct2py celery pygal
RUN sed -i 's/pyamqp:\/\//pyamqp:\/\/admin:password@rabbitmq:5672/' ./celery_app.py
RUN sed -i 's/\/home\/ubuntu\/BENCHOPaaS\/BENCHOP\/BENCHOP/\/home\/fedora\/BENCHOP/' ./tasks.py
ENV FLASK_APP=flask_app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
