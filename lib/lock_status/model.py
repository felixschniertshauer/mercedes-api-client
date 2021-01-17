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
class ResourceMetaInfo(DataClassJsonMixin):
    """ ResourceMetaInfo """
    
    href: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VehicleLockStatus(DataClassJsonMixin):
    """ VehicleLockStatus """
    
    doorlockstatusdecklid: Optional[Resource] = None
    """ Resource """
    
    doorlockstatusgas: Optional[Resource] = None
    """ Resource """
    
    doorlockstatusvehicle: Optional[Resource] = None
    """ Resource """
    
    position_heading: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestDoorLockStatusdeckLidUsingGETResponse(DataClassJsonMixin):
    doorlockstatusdecklid: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestDoorLockStatusGasUsingGETResponse(DataClassJsonMixin):
    doorlockstatusgas: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestDoorLockStatusUsingGETResponse(DataClassJsonMixin):
    doorlockstatusvehicle: Optional[Resource] = None
    """ Resource """
    

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetLatestPositionHeadingUsingGETResponse(DataClassJsonMixin):
    position_heading: Optional[Resource] = None
    """ Resource """
    


__all__ = \
[
    'ExVeError',
    'GetLatestDoorLockStatusGasUsingGETResponse',
    'GetLatestDoorLockStatusUsingGETResponse',
    'GetLatestDoorLockStatusdeckLidUsingGETResponse',
    'GetLatestPositionHeadingUsingGETResponse',
    'Resource',
    'ResourceMetaInfo',
    'VehicleLockStatus',
]
