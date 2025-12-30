FROM python:3.9-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords punkt

COPY . .

# API port
EXPOSE 8000 
# Streamlit port
EXPOSE 8501

RUN echo "#!/bin/bash\n\
export PYTHONPATH=/app\n\
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &\n\
streamlit run src/UI/mainUI.py --server.port 8501 --server.address 0.0.0.0\n\
" > /app/run.sh

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]