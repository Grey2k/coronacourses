# Init image
FROM python:3.8
RUN pip install --upgrade pip && \
    mkdir -p /app

# Copy and install app
WORKDIR /app
COPY . /app/
RUN rm -rf venv && \
    pip install --upgrade .

# Export
CMD ["./startup.sh"]
EXPOSE 8080