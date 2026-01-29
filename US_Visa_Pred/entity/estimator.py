import os,sys
import numpy as np

from US_Visa_Pred.exceptions.exception import CustomException
from US_Visa_Pred.logger.logging import logging

class TargetValue:
    def __init__(self) -> None:
        self.Certified:int = 0
        self.Denied:int = 1
    def _asdict(self):
        return self.__dict__
    def reverse_map(self):
        mapping = self._asdict()
        return dict(zip(mapping.values(),mapping.keys()))
    
    