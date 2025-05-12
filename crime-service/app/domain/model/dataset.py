from dataclasses import dataclass
from flask import json
import googlemaps
import pandas as pd

@dataclass
class Dataset:
    cctv : object
    crime : object
    pop : object
    police : object
    

    @property
    def cctv(self) -> object:
        return self._cctv
    
    @cctv.setter
    def cctv(self, cctv):
        self._cctv = cctv
    
    @property
    def crime(self) -> object:
        return self._crime
    
    @crime.setter
    def crime(self, crime):
        self._crime = crime
    
    @property
    def pop(self) -> object:
        return self._pop
    
    @pop.setter
    def pop(self, pop):
        self._pop = pop

    @property
    def police(self) -> object:
        return self._police
    
    @police.setter
    def police(self, police):
        self._police = police
    
    