FROM python:3.7.0

# Create project folder
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Add code
COPY ./src /app/src