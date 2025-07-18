#code to interface with the build module 
#we are going to use the uuid generator but return the uuid python types

import uuid
import _uuidcffi

_ffi = _uuicdffi.ffi
_lib = _uuidcffi.lib

def generate_uuid() -> uuid.UUID:
  #use the ffi library to construct various types
  
