FROM jaspajjr/data-science-dockerfile

COPY requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt

COPY ./src /data

COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry

CMD ["start"]
ENTRYPOINT ["/entry"]
