FROM python:3.7.2
ADD dc-logs-generator.py /

CMD ["python3", "-u", "./dc-logs-generator.py"]
