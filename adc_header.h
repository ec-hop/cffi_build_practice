#include <stdint.h>

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
