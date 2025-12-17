FROM python:3.14-slim

WORKDIR /app

COPY ./night-cli /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV Streamlit-app=main.py

CMD ["streamlit","run","--host=0.0.0.0"]

