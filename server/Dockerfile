FROM python
 
# Set the working directory to /usr/src/app.
WORKDIR /usr/src/app
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip install -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

EXPOSE 8080
# Run the crawler when the container launches.
CMD [ "python", "./serve.py" ]