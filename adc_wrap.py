from cffi import FFI

ffi = FFI()

ffi.cdef("""
    typedef struct {
        int adc_bits;
        float v_ref;
        float noise_stddev;
    } ADCConfig;

    ADCConfig* adc_create(int bits, float v_ref, float noise_stddev);
    void adc_free(ADCConfig* config);
    uint16_t adc_sample(float input_voltage, ADCConfig* config);
    void adc_set_bits(ADCConfig* config, int bits);
    void adc_set_vref(ADCConfig* config, float v_ref);
    void adc_set_noise(ADCConfig* config, float noise_stddev);
""")

C = ffi.dlopen("./libadc.so")  # Make sure you've compiled libadc.c to libadc.so

class ADC:
    def __init__(self, bits=12, vref=3.3, noise=0.01):
        self._cfg = C.adc_create(bits, vref, noise)
        if self._cfg == ffi.NULL:
            raise ValueError("Invalid ADC configuration")

    def __del__(self):
        if hasattr(self, "_cfg") and self._cfg != ffi.NULL:
            C.adc_free(self._cfg)
            self._cfg = ffi.NULL

    def sample(self, voltage):
        return C.adc_sample(voltage, self._cfg)

    def set_resolution(self, bits):
        C.adc_set_bits(self._cfg, bits)

    def set_vref(self, vref):
        C.adc_set_vref(self._cfg, vref)

    def set_noise(self, noise_stddev):
        C.adc_set_noise(self._cfg, noise_stddev)
