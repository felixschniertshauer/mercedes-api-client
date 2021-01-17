from .utils import datetime_decoder
from .utils import discriminator_decoder
from dataclasses import dataclass
from dataclasses import field
from dataclasses_json.api import DataClassJsonMixin
from dataclasses_json.api import LetterCase
from dataclasses_json.api import dataclass_json
from dataclasses_json.cfg import config
from datetime import date
from datetime import datetime
from datetime import time
from enum import Enum
from typing import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ExVeError(DataClassJsonMixin):
    """ ExVeError """
    
    exve_error_id: Optional[str] = None
    exve_error_msg: Optional[str] = None
    exve_error_ref: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Resource(DataClassJsonMixin):
    """ Resource """
    
    timestamp: Optional[int] = None
    value: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FuelStatus(DataClassJsonMixin):
    """ FuelStatus """
    
    rangeliquid: Optional[Resource] = None
    """ Resource """
    
    tanklevelpercent: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ResourceMetaInfo(DataClassJsonMixin):
    """ ResourceMetaInfo """
    
    href: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestRangeliquidUsingGETResponse(DataClassJsonMixin):
    rangeliquid: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestTankLevelUsingGETResponse(DataClassJsonMixin):
    tanklevelpercent: Optional[Resource] = None
    """ Resource """
    


__all__ = \
[
    'ExVeError',
    'FuelStatus',
    'GetLatestRangeliquidUsingGETResponse',
    'GetLatestTankLevelUsingGETResponse',
    'Resource',
    'ResourceMetaInfo',
]
