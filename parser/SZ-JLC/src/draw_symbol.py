#!/usr/bin/env python3
import os,sys,re
from constant import *


SMD_CAPACITOR_SYMBOL='''
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
'''.strip()

SMD_RESISTOR_SYMBOL='''
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
'''.strip()

SMD_INDUCTOR_SYMBOL='''
A 0 -60 20 -899 899 0 1 0 N 0 -80 0 -40
A 0 -20 20 -899 899 0 1 0 N 0 -40 0 0
A 0 20 20 -899 899 0 1 0 N 0 0 0 40
A 0 60 20 -899 899 0 1 0 N 0 40 0 80
X ~ 1 0 100 20 D 50 50 1 1 P
X ~ 2 0 -100 20 U 50 50 1 1 P
'''.strip()

SMD_LED_SYMBOL='''
P 2 0 1 0 -30 -40 -30 40 N
P 2 0 1 0 40 0 -30 0 N
P 4 0 1 0 30 -40 -30 0 30 40 30 -40 N
P 5 0 1 0 0 30 -20 50 -10 50 -20 50 -20 40 N
P 5 0 1 0 20 50 0 70 10 70 0 70 0 60 N
X K 1 -100 0 70 R 50 50 1 1 P
X A 2 100 0 70 L 50 50 1 1 P
'''.strip()

SMD_DIODE_SYMBOL='''
P 2 0 1 0 -30 -40 -30 40 N
P 2 0 1 0 -30 0 30 0 N
P 4 0 1 0 30 -40 -30 0 30 40 30 -40 N
X K 1 -100 0 70 R 50 50 1 1 P
X A 2 100 0 70 L 50 50 1 1 P
'''.strip()

SMD_LDO_SYMBOL='''
S -200 -200 200 75 0 1 10 f
X ADJ 1 0 -300 100 U 50 50 1 1 I
X VO 2 300 0 100 L 50 50 1 1 w
X VI 3 -300 0 100 R 50 50 1 1 W
'''.strip()

SMD_MICROCONTROLLER_MCU_SYMBOL='''
T 0 0 -400 50 0 0 0 DEFAULT Normal 0 C C
S -800 800 750 -750 0 1 0 f
'''.strip()

SMD_DEFAULT_SYMBOL='''
T 0 0 -400 50 0 0 0 DEFAULT Normal 0 C C
S -800 800 750 -750 0 1 0 f
'''.strip()

SMD_LED_SYMBOL='''
P 2 0 1 0 -30 -40 -30 40 N
P 2 0 1 0 40 0 -30 0 N
P 4 0 1 0 30 -40 -30 0 30 40 30 -40 N
P 5 0 1 0 0 30 -20 50 -10 50 -20 50 -20 40 N
P 5 0 1 0 20 50 0 70 10 70 0 70 0 60 N
X K 1 -100 0 70 R 50 50 1 1 P
X A 2 100 0 70 L 50 50 1 1 P
'''.strip()

SMD_AMPLIFIER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ACTIVE_FILTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_AMBIENT_LIGHT_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ACCELEROMETER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ACTIVE_CRYSTAL_OSCILLATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ANALOG_SWITCH_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ANALOG_TO_DIGITAL_CONVERSION_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ANGLE_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ANGULAR_VELOCITY_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ATTITUDE_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_AUDIO_POWER_AMPLIFIER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BALANCED_UNBALANCED_TRANSFORMER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BALLAST_CONTROLLER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BATTERY_BOX_BATTERY_HOLDER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BATTERY_POWER_MANAGEMENT_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BATTERY_PROTECTION_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CAN_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CERAMIC_RESONATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CLOCK_BUFFER_DRIVER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CLOCK_GENERATOR_PLL_FREQUENCY_SYNTHESIZER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CLOCK_TIMING_DEDICATED_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CODEC_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_COLOR_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_COMMON_MODE_INDUCTOR_FILTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CONSTANT_CURRENT_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CONSTANT_CURRENT_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_COUNTER_DIVIDER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CPLD_FPGA_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CURRENT_MONITORING_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_CURRENT_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DARLINGTON_TRANSISTOR_ARRAY_DRIVE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DARLINGTON_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DC_DC_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DDR_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DDS_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DEDICATED_SENSORS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DIFFERENTIAL_OP_AMPS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DIGITAL_POTENTIOMETER_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DIGITAL_TO_ANALOG_CONVERSION_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DISCHARGE_TUBE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DISPOSABLE_FUSES_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_DRIVER_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_EEPROM_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_EL_DRIVE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ELECTROLYTIC_CAPACITORS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_EMI_RFI_FILTERS_LC_RC_NETWORKS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_EPROM_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ETHERNET_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FAST_RECOVERY_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FAST_RECOVERY_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FET_INPUT_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FLASH_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FONT_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FRAM_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FUEL_GAUGE_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_FULL_BRIDGE_HALF_BRIDGE_DRIVE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_GAS_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_GATE_AND_INVERTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_HF_INDUCTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_HIGH_EFFICIENCY_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_HIGH_PRESISION_RESISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_HIGH_SPEED_BROADBAND_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_HIGH_VOLTAGE_RESISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_I_O_EXPANDER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_IGBT_DRIVE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_IGBT_TUBE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INFRARED_EMISSION_TUBE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INFRARED_RECEIVER_TUBE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INFRARED_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INSTRUMENT_OPERATIONAL_AMPLIFIER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INTERFACE_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INTERFACE_CONTROLLER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INTERFACE_DEDICATED_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INTERFACE_LIN_TRANSCEIVER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_INTERFACE_TELECOM_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ISOLATOR_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_JFET_JUNCTION_FIELD_EFFECT_TRANSISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LATCHES_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LCD_DRIVER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LEVEL_SHIFTER_SHIFTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LINEAR_VOLTAGE_REGULATOR_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LOGIC_CHIP__SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LOGIC_CHIP_4000_SERIES_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LOGIC_CHIP_74_SERIES_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LOW_NOISE_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LOW_POWER_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_LVDS_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MAGNETIC_BEADS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MAGNETIC_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MOS_DRIVE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MOS_FIELD_EFFECT_TUBE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MOTOR_DRIVER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_MULTI_FREQUENCY_OSCILLATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_NETWORK_PORT_TRANSFORMER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_NIOBIUM_OXIDE_CAPACITOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_NTC_RESISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_OP_AMP_GENERAL_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_OP_AMP_PRECISION_OP_AMP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_OPTICAL_SENSORS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_OPTOCOUPLER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PASSIVE_CRYSTAL_RESONATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PHOTOELECTRIC_SOLID_STATE_RELAY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PHOTOELECTRIC_SWITCH_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PHOTOELECTRIC_TRIAC_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PORT_EXPANSION_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_POSITION_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_POWER_INDUCTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_POWER_MONITORING_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_POWER_SWITCH_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PRESSURE_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PROFESSIONAL_POWER_MANAGEMENT_PMIC_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_PTC_RESETTABLE_FUSE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_REAL_TIME_CLOCK_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RECTIFIER_BRIDGE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RESISTOR_NETWORK_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_AMPLIFIER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_ATTENUATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_CARD_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_COUPLER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_DETECTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_FILTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_MIXER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RF_SWITCH_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RS232_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_RS485_RS422_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SCHOTTKY_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SDRAM_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SECURITY_VERIFICATION_ENCRYPTION_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SENSOR_INTERFACE_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SERIAL_INTERFACE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SHIFT_REGISTER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SIGNAL_BUFFERS_REPEATERS_DISTRIBUTORS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SOLID_ELECTROLYTIC_CAPACITOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SOUND_SURFACE_RESONATOR_SAW_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SPECIAL_FUNCTION_AMPLIFIER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SPECIAL_FUNCTION_DRIVEN_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SRAM_MEMORY_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SWITCHING_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_SWITCHING_POWER_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TACT_SWITCH_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TANTALUM_CAPACITOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TEMPERATURE_AND_HUMIDITY_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TEMPERATURE_SENSOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_THYRISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TIME_BASE_INTEGRATED_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TOUCH_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TOUCH_SCREEN_CONTROLLER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TRIGGER_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TRIGGER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TRIODE_DIGITAL_TRIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TRIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_TVS_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_ULTRA_FAST_RECOVERY_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_USB_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VARICAP_DIODE_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VARISTOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VIDEO_AND_AUDIO_INTERFACE_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VIDEO_FILTER_DRIVER_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VOLTAGE_COMPARATOR_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_VOLTAGE_REFERENCE_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL
SMD_WIRELESS_TRANSCEIVER_CHIP_SYMBOL=SMD_DEFAULT_SYMBOL

def lookup_drawing(component_category_in):
  return component_drawing[component_category_in]
