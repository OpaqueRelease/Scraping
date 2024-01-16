# FROM postgres:15.1-alpine

# COPY *.sql /docker-entrypoint-initdb.d/
# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python
 
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip install -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .
 
# Run the crawler when the container launches.
CMD [ "python", "./go-spider.py" ]