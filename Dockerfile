# FROM python:3.7-slim

# RUN pip install pipenv
# # RUN cd /my/app/path && pipenv install

# ENV SRC_DIR /Users/andre22/Documents/Dev/Intensive_projects/Startup-Predictor

# WORKDIR ${SRC_DIR}

# COPY Pipfile Pipfile.lock ${SRC_DIR}/

# RUN pipenv install --deploy --ignore-pipfile

# COPY ./ ${SRC_DIR}/

# WORKDIR ${SRC_DIR}

# #Open port 5000 
# EXPOSE 5000

# CMD ["pipenv", "run", "python", "app.py"]


#Use python as base image
FROM python:3.7-slim

#Use working directory /app
WORKDIR /app

#Copy all the content of current directory to /app
ADD . /app

#Installing required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN pip install pipenv 

# RUN pipenv install --system --deploy

#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python","app.py"]

# FROM python:3.7-slim
# COPY . /app
# WORKDIR /app

# RUN pip install pipenv

# RUN pipenv install --system --deploy

# EXPOSE 5000

# CMD ["python", "app.py"]




#Use python as base image
# FROM python:3.7-slim

# #Use working directory /app
# WORKDIR /app

# #Copy all the content of current directory to /app
# ADD . /app

# #Installing required packages
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# #Open port 5000
# EXPOSE 5000

# #Set environment variable
# ENV NAME OpentoAll

# #Run python program
# CMD ["python","app.py"]