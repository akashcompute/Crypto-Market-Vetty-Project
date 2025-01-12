FROM python:3.9-slim
LABEL authors="akash.kumar"

# Set the working directory in the container
WORKDIR /app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
