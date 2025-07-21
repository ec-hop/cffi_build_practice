#include "libadc.h"
#include <stdlib.h>

float apply_noise(float val, float stddev) {
    float r = ((float)rand() / RAND_MAX) * 2.0f - 1.0f;
    return val + r * stddev;
}

uint16_t adc_sample(float input_voltage, ADCConfig* config) {
    float noisy = apply_noise(input_voltage, config->noise_stddev);
    if (noisy > config->v_ref) noisy = config->v_ref;
    if (noisy < 0.0f) noisy = 0.0f;

    int max_val = (1 << config->adc_bits) - 1;
    return (uint16_t)((noisy / config->v_ref) * max_val);
}

ADCConfig* adc_create(int bits, float v_ref, float noise_stddev) {
    if (bits < 8 || bits > 16) return NULL;
    ADCConfig* cfg = (ADCConfig*)malloc(sizeof(ADCConfig));
    cfg->adc_bits = bits;
    cfg->v_ref = v_ref;
    cfg->noise_stddev = noise_stddev;
    return cfg;
}

void adc_free(ADCConfig* config) {
    free(config);
}

void adc_set_bits(ADCConfig* config, int bits) {
    if (bits >= 8 && bits <= 16)
        config->adc_bits = bits;
}

void adc_set_vref(ADCConfig* config, float v_ref) {
    config->v_ref = v_ref;
}

void adc_set_noise(ADCConfig* config, float noise_stddev) {
    config->noise_stddev = noise_stddev;
}
