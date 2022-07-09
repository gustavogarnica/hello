FROM python
ADD hello.py /hello.py
ENTRYPOINT ["python", "hello.py"]
