# "the magic that makes the ffi module work"

#in order to build this module, we need to import some parts of the CFFI module & 
#it will do most of the magic for us

from cffi import ffi

CDEF = ```\
typedef unsigned char uuid_t[16]:

void uuid_generate(uuid_t out): #we need to make the uuid generate function available to the cffi
```

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
  "uuidcffi",
  "#include <uuid/uuid.h>", #need to tell where to find all the C declarations
  libraries =["uuid"], 
  #need to tell it to link against the uuid library&
)
