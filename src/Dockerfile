FROM python
WORKDIR /app
#COPY ../main.py ./src/app
#COPY /BusinessCard/main.py .
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python", "main.py"]
EXPOSE 5000