#define REF_ADS1298_REG_DEFS
#ifdef REF_ADS1298_REG_DEFS

#include <stdint.h> 

typedef struct{ 
uint8_t id;
uint8_t config1;
uint8_t config2;
} ref_ads1298_t; 

#define REF_ADS1298_ID_DEV_ID_MASK  0X07
#define REF_ADS1298_ID_DEV_ID_SHIFT_VAL  0

#define REF_ADS1298_ID_DEV_CHN_ID_MASK  0XE0
#define REF_ADS1298_ID_DEV_CHN_ID_SHIFT_VAL  5

#define REF_ADS1298_CONFIG1_DR_MASK  0X07
#define REF_ADS1298_CONFIG1_DR_SHIFT_VAL  0

#define REF_ADS1298_CONFIG1_CLK_EN_MASK  0X20
#define REF_ADS1298_CONFIG1_CLK_EN_SHIFT_VAL  5

#define REF_ADS1298_CONFIG1_DAISY_EN_MASK  0X40
#define REF_ADS1298_CONFIG1_DAISY_EN_SHIFT_VAL  6

#define REF_ADS1298_CONFIG1_HR_MASK  0X80
#define REF_ADS1298_CONFIG1_HR_SHIFT_VAL  7

#define REF_ADS1298_CONFIG2_TEST_FREQ_MASK  0X03
#define REF_ADS1298_CONFIG2_TEST_FREQ_SHIFT_VAL  0

#define REF_ADS1298_CONFIG2_TEST_AMP_MASK  0X04
#define REF_ADS1298_CONFIG2_TEST_AMP_SHIFT_VAL  2

#define REF_ADS1298_CONFIG2_INT_TEST_MASK  0X10
#define REF_ADS1298_CONFIG2_INT_TEST_SHIFT_VAL  4

#define REF_ADS1298_CONFIG2_WCT_CHOP_MASK  0X20
#define REF_ADS1298_CONFIG2_WCT_CHOP_SHIFT_VAL  5





#endif //REF_ADS1298_REG_DEFS
