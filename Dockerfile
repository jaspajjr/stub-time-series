FROM jaspajjr/data-science-dockerfile

RUN chmod +x /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
RUN mkdir /output

COPY ./HRA /data/HRA
COPY ./start.py /data/start.py
COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry

CMD ["start"]
ENTRYPOINT ["/entry"]
