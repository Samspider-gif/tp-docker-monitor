FROM python:3.9-alpine
RUN adduser -D myuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
# Permissions sur le dossier logs
RUN mkdir logs && chown -R myuser:myuser /app/logs
USER myuser
EXPOSE 5000
CMD ["python", "app.py"]
