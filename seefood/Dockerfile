{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Use python 3.10 slim version\
FROM python:3.10-slim\
\
# Set working directory\
WORKDIR /app\
\
# Copy requirements and install\
COPY requirements.txt .\
RUN pip install --no-cache-dir -r requirements.txt\
\
# Copy the rest of the application\
COPY . .\
\
# Expose port 8000\
EXPOSE 8000\
\
# Run the app\
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]}