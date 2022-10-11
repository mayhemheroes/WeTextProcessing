FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /WeTextProcessing
WORKDIR /WeTextProcessing
RUN python3 -m pip install -r requirements.txt && python3 setup.py sdist bdist_wheel --version=1 && python3 -m pip install dist/WeTextProcessing-1-py3-none-any.whl && chmod +x fuzz/text_processing_fuzz.py

ENTRYPOINT [ ]
CMD ["/WeTextProcessing/fuzz/text_processing_fuzz.py"]