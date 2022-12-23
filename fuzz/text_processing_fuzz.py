#!/usr/local/bin/python3
import atheris
import sys
import io
import os

# with atheris.instrument_imports():
from tn.chinese.normalizer import Normalizer
from itn.chinese.inverse_normalizer import InverseNormalizer

normalizer = Normalizer()
invnormalizer = InverseNormalizer()


@atheris.instrument_func
def TestOneInput(data):
    if len(data) > 0:
        fdp = atheris.FuzzedDataProvider(data)
        opt = fdp.ConsumeInt(1) % 2
        in_string = fdp.ConsumeUnicode(len(data))
        if opt == 0:
            normalizer.normalize(in_string)
        else:
            invnormalizer.normalize(in_string)
        
        
atheris.Setup(sys.argv, TestOneInput)
atheris.instrument_all()
atheris.Fuzz()