FROM python:3.8

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install google-cloud-bigquery

COPY app app
WORKDIR /app
RUN pip install -r requirements.txt

# # streamlitように
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]