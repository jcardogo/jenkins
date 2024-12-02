FROM python:3.9
COPY *.py setup.cfg LICENSE README.md requirement.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python setup.py install 
EXPOSE 8000
CMD ["/usr/local/bin/my-application"]
