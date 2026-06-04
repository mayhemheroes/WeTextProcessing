FROM python:3.11-slim

RUN apt-get update && apt-get install -y clang && rm -rf /var/lib/apt/lists/*
RUN pip3 install atheris

COPY . /WeTextProcessing
WORKDIR /WeTextProcessing
RUN python3 -m pip install -r requirements.txt && python3 setup.py sdist bdist_wheel --version=1 && python3 -m pip install dist/*.whl && chmod +x fuzz/text_processing_fuzz.py

ENTRYPOINT [ ]
CMD ["/WeTextProcessing/fuzz/text_processing_fuzz.py"]
