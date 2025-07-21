# cffi_build_practice
Practicing linking libraries and building compatible wrappers

Following tutorial by anthonywritescode: https://www.youtube.com/watch?v=X5irxO5VCHw
  - build, setup, and uuidcffi are apart of this tutorial.

Separate ADC logic algorithm cffi wrapper practice is included. 

Eventual goal is to be proficient at wrappers and cffi for efficient code integration for AMD GPU's. 


For ADC wrapper:

compilation: gcc -shared -fPIC -o libadc.so libadc.c

adc_wrap is a Python CFFI wrapper around a lightweight C library that simulates an analog-to-digital converter (ADC). Goal of library is for testing signal processing pipelines and simulating embedded ADC inputs without the hardware. 
