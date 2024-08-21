# Use the official Python image from the Docker Hub
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy all contents from the app directory to /app in the container
COPY app/ /app/

# Expose the necessary ports
EXPOSE 3000
EXPOSE 5000

# Run the Flask applications
CMD ["sh", "-c", "python slackbot.py & python bot.py"]
