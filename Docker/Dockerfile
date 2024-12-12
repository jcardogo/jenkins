#FROM sets the base image to use. In this case, we are using the Python 3.9 base image.
FROM python:3.9 
#WORKDIR sets the working directory inside the image.
WORKDIR /app 
#COPY requirements.txt ./ copies the requirements.txt file to the working directory.
COPY requirements.txt ./ 
#RUN pip install -r requirements.txt installs the requirements.
RUN pip install -r requirements.txt 
#COPY . . copies all the files in the current directory to the working directory.
COPY . . 
#EXPOSE 4000 exposes the port 4000.
EXPOSE 4000 
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"] tells Docker to run Flask when the container starts.
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"] 