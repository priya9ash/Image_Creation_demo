#to buikd the base image which we got from the dockerhub which has has an OS and python installed
FROM python:3.11-slim 
# in that mini computer , create a folder called flask-docker
WORKDIR /flask-docker

#since my python verion is old , upgrade my pip
RUN python3 -m pip install --upgrade pip
#copy the requirements.txt file from the local folder to the folder in that mini computer 
COPY requirements.txt requirements.txt
# run the pip install to install the requirement.txt in the mini computer 
RUN pip3 install -r requirements.txt


COPY . .
CMD ["python3","-m","flask","run","--host=0.0.0.0"]