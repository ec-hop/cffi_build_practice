#code to interface with the build module 
#we are going to use the uuid generator but return the uuid python types

import uuid
import _uuidcffi

_ffi = _uuidcffi.ffi
_lib = _uuidcffi.lib

def generate_uuid() -> uuid.UUID:
  #use the ffi library to construct various types
  buf = _ffi.new("uuid_t") # ffi.new will manage creating type and deleting when out of scope
  _lib.uuid_generate(buf)
  return uuid.UUID(bytes= bytes(buf))


                  
                   
