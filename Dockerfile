FROM python:3.8
RUN pip3 install selenium requests
COPY extract.py /
COPY chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver
WORKDIR /
CMD ["python", "extract.py"]
