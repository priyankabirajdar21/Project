FROM python:3.7.5
RUN pip install -U nltk 
RUN pip install -U numpy 
RUN pip3 install -U bs4
RUN pip3 install -U networkx
RUN pip3 install -U scipy
#RUN pip install -U urllib2

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords






WORKDIR /usr/src/app

COPY . .

ENTRYPOINT [ "python3", "text_summ.py" ]

CMD [ "IP"]
