from setuptools import setup

setup(
  name= "uuidcffi",
  version= "1",
  py_modules= ["uuidcffi"],
  install_requires=["cffi"], #these are the dependencies we will have at run time
  setup_requires = ["cffi"], #dependencies for build times
  cffi_modules=["build_uuidcffi.py:ffibuilder], #tells to build -takes entrypoint like things
  )

