#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from footprint_table import *
from footprint_list_table import *
from master_table import *

# footprint_lookup_dic={
#   # CAT_SMD_ACTIVE_FILTER:[active_filter_footprint_expand, active_filter_footprint_list_expand],
#   # CAT_SMD_ACTIVE_FILTER:[active_filter_footprint_expand, active_filter_footprint_list_expand],
#   # CAT_SMD_AMBIENT_LIGHT_SENSOR:[ambient_light_sensor_footprint_expand, ambient_light_sensor_footprint_list_expand],
#   # CAT_SMD_AMPLIFIER:[amplifier_footprint_expand, amplifier_footprint_list_expand],
#   # CAT_SMD_ANALOG_SWITCH_CHIP:[analog_switch_chip_footprint_expand, analog_switch_chip_footprint_list_expand],
#   # CAT_SMD_ANALOG_TO_DIGITAL_CONVERSION_CHIP:[analog_to_digital_conversion_chip_footprint_expand, analog_to_digital_conversion_chip_footprint_list_expand],
#   # CAT_SMD_ANGLE_SENSOR:[angle_sensor_footprint_expand, angle_sensor_footprint_list_expand],
#   # CAT_SMD_ANGULAR_VELOCITY_SENSOR:[angular_velocity_sensor_footprint_expand, angular_velocity_sensor_footprint_list_expand],
#   # CAT_SMD_ATTITUDE_SENSOR:[attitude_sensor_footprint_expand, attitude_sensor_footprint_list_expand],
#   # CAT_SMD_AUDIO_POWER_AMPLIFIER:[audio_power_amplifier_footprint_expand, audio_power_amplifier_footprint_list_expand],
#   # CAT_SMD_AVALANCHE_DIODE:[avalanche_diode_footprint_expand, avalanche_diode_footprint_list_expand],
#   # CAT_SMD_BALANCED_UNBALANCED_TRANSFORMER:[balanced_unbalanced_transformer_footprint_expand, balanced_unbalanced_transformer_footprint_list_expand],
#   # CAT_SMD_BALLAST_CONTROLLER:[ballast_controller_footprint_expand, ballast_controller_footprint_list_expand],
#   # CAT_SMD_BATTERY_BOX_BATTERY_HOLDER:[battery_box_battery_holder_footprint_expand, battery_box_battery_holder_footprint_list_expand],
#   # CAT_SMD_BATTERY_POWER_MANAGEMENT_CHIP:[battery_power_management_chip_footprint_expand, battery_power_management_chip_footprint_list_expand],
#   # CAT_SMD_BATTERY_PROTECTION_CHIP:[battery_protection_chip_footprint_expand, battery_protection_chip_footprint_list_expand],
#   # CAT_SMD_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS:[buffers_drivers_receivers_transceivers_footprint_expand, buffers_drivers_receivers_transceivers_footprint_list_expand],
#   # CAT_SMD_CAN_CHIP:[can_chip_footprint_expand, can_chip_footprint_list_expand],
#   # CAT_SMD_CAPACITOR:[capacitor_footprint_expand, capacitor_footprint_list_expand],
#   # CAT_SMD_CERAMIC_RESONATOR:[ceramic_resonator_footprint_expand, ceramic_resonator_footprint_list_expand],
#   # CAT_SMD_CLOCK_BUFFER_DRIVER:[clock_buffer_driver_footprint_expand, clock_buffer_driver_footprint_list_expand],
#   # CAT_SMD_CLOCK_GENERATOR_PLL_FREQUENCY_SYNTHESIZER:[clock_generator_pll_frequency_synthesizer_footprint_expand, clock_generator_pll_frequency_synthesizer_footprint_list_expand],
#   # CAT_SMD_CLOCK_TIMING_DEDICATED:[clock_timing_dedicated_footprint_expand, clock_timing_dedicated_footprint_list_expand],
#   # CAT_SMD_CODEC_CHIP:[codec_chip_footprint_expand, codec_chip_footprint_list_expand],
#   # CAT_SMD_COLOR_SENSOR:[color_sensor_footprint_expand, color_sensor_footprint_list_expand],
#   # CAT_SMD_COMMON_MODE_INDUCTOR_FILTER:[common_mode_inductor_filter_footprint_expand, common_mode_inductor_filter_footprint_list_expand],
#   # CAT_SMD_CONSTANT_CURRENT_DIODE:[constant_current_diode_footprint_expand, constant_current_diode_footprint_list_expand],
#   # CAT_SMD_CONSTANT_CURRENT_DIODE:[constant_current_diode_footprint_expand, constant_current_diode_footprint_list_expand],
#   # CAT_SMD_COUNTER_DIVIDER:[counter_divider_footprint_expand, counter_divider_footprint_list_expand],
#   # CAT_SMD_CPLD_FPGA_CHIP:[cpld_fpga_chip_footprint_expand, cpld_fpga_chip_footprint_list_expand],
#   # CAT_SMD_CURRENT_MONITORING_CHIP:[current_monitoring_chip_footprint_expand, current_monitoring_chip_footprint_list_expand],
#   # CAT_SMD_CURRENT_SENSOR:[current_sensor_footprint_expand, current_sensor_footprint_list_expand],
#   # CAT_SMD_DARLINGTON_TRANSISTOR_ARRAY_DRIVE:[darlington_transistor_array_drive_footprint_expand, darlington_transistor_array_drive_footprint_list_expand],
#   # CAT_SMD_DARLINGTON:[darlington_footprint_expand, darlington_footprint_list_expand],
#   # CAT_SMD_DC_DC_CHIP:[dc_dc_chip_footprint_expand, dc_dc_chip_footprint_list_expand],
#   # CAT_SMD_DDR_MEMORY:[ddr_memory_footprint_expand, ddr_memory_footprint_list_expand],
#   # CAT_SMD_DDS_CHIP:[dds_chip_footprint_expand, dds_chip_footprint_list_expand],
#   # CAT_SMD_DEDICATED_SENSORS:[dedicated_sensors_footprint_expand, dedicated_sensors_footprint_list_expand],
#   # CAT_SMD_DIFFERENTIAL_OP_AMPS:[differential_op_amps_footprint_expand, differential_op_amps_footprint_list_expand],
#   # CAT_SMD_DIGITAL_POTENTIOMETER_CHIP:[digital_potentiometer_chip_footprint_expand, digital_potentiometer_chip_footprint_list_expand],
#   # CAT_SMD_DIGITAL_TO_ANALOG_CONVERSION_CHIP:[digital_to_analog_conversion_chip_footprint_expand, digital_to_analog_conversion_chip_footprint_list_expand],
#   # CAT_SMD_DIODE:[diode_footprint_expand, diode_footprint_list_expand],
#   # CAT_SMD_DISCHARGE_TUBE:[discharge_tube_footprint_expand, discharge_tube_footprint_list_expand],
#   # CAT_SMD_DISPOSABLE_FUSES:[disposable_fuses_footprint_expand, disposable_fuses_footprint_list_expand],
#   # CAT_SMD_DRIVER_CHIP:[driver_chip_footprint_expand, driver_chip_footprint_list_expand],
#   # CAT_SMD_EEPROM_MEMORY:[eeprom_memory_footprint_expand, eeprom_memory_footprint_list_expand],
#   # CAT_SMD_EL_DRIVE:[el_drive_footprint_expand, el_drive_footprint_list_expand],
#   # CAT_SMD_ELECTROLYTIC_CAPACITORS:[electrolytic_capacitors_footprint_expand, electrolytic_capacitors_footprint_list_expand],
#   # CAT_SMD_EMI_RFI_FILTERS_LC_RC_NETWORKS:[emi_rfi_filters_lc_rc_networks_footprint_expand, emi_rfi_filters_lc_rc_networks_footprint_list_expand],
#   # CAT_SMD_EPROM_MEMORY:[eprom_memory_footprint_expand, eprom_memory_footprint_list_expand],
#   # CAT_SMD_ETHERNET_CHIP:[ethernet_chip_footprint_expand, ethernet_chip_footprint_list_expand],
#   # CAT_SMD_FAST_RECOVERY_DIODE:[fast_recovery_diode_footprint_expand, fast_recovery_diode_footprint_list_expand],
#   # CAT_SMD_FET_INPUT_OP_AMP:[fet_input_op_amp_footprint_expand, fet_input_op_amp_footprint_list_expand],
#   # CAT_SMD_FLASH_MEMORY:[flash_memory_footprint_expand, flash_memory_footprint_list_expand],
#   # CAT_SMD_FONT_CHIP:[font_chip_footprint_expand, font_chip_footprint_list_expand],
#   # CAT_SMD_FRAM_MEMORY:[fram_memory_footprint_expand, fram_memory_footprint_list_expand],
#   # CAT_SMD_FUEL_GAUGE_CHIP:[fuel_gauge_chip_footprint_expand, fuel_gauge_chip_footprint_list_expand],
#   # CAT_SMD_FULL_BRIDGE_HALF_BRIDGE_DRIVE:[full_bridge_half_bridge_drive_footprint_expand, full_bridge_half_bridge_drive_footprint_list_expand],
#   # CAT_SMD_GAS_SENSOR:[gas_sensor_footprint_expand, gas_sensor_footprint_list_expand],
#   # CAT_SMD_GATE_AND_INVERTER:[gate_and_inverter_footprint_expand, gate_and_inverter_footprint_list_expand],
#   # CAT_SMD_HF_INDUCTOR:[hf_inductor_footprint_expand, hf_inductor_footprint_list_expand],
#   # CAT_SMD_HIGH_PRESISION_RESISTOR:[high_presision_resistor_footprint_expand, high_presision_resistor_footprint_list_expand],
#   # CAT_SMD_HIGH_SPEED_BROADBAND_OP_AMP:[high_speed_broadband_op_amp_footprint_expand, high_speed_broadband_op_amp_footprint_list_expand],
#   # CAT_SMD_HIGH_VOLTAGE_RESISTOR:[high_voltage_resistor_footprint_expand, high_voltage_resistor_footprint_list_expand],
#   # CAT_SMD_I_O_EXPANDER:[i_o_expander_footprint_expand, i_o_expander_footprint_list_expand],
#   # CAT_SMD_IGBT_DRIVE:[igbt_drive_footprint_expand, igbt_drive_footprint_list_expand],
#   # CAT_SMD_IGBT_TUBE:[igbt_tube_footprint_expand, igbt_tube_footprint_list_expand],
#   # CAT_SMD_INFRARED_EMISSION_TUBE:[infrared_emission_tube_footprint_expand, infrared_emission_tube_footprint_list_expand],
#   # CAT_SMD_INFRARED_RECEIVER_TUBE:[infrared_receiver_tube_footprint_expand, infrared_receiver_tube_footprint_list_expand],
#   # CAT_SMD_INFRARED_SENSOR:[infrared_sensor_footprint_expand, infrared_sensor_footprint_list_expand],
#   # CAT_SMD_INSTRUMENT_OPERATIONAL_AMPLIFIER:[instrument_operational_amplifier_footprint_expand, instrument_operational_amplifier_footprint_list_expand],
#   # CAT_SMD_INTERFACE_CHIP:[interface_chip_footprint_expand, interface_chip_footprint_list_expand],
#   # CAT_SMD_INTERFACE_CONTROLLER:[interface_controller_footprint_expand, interface_controller_footprint_list_expand],
#   # CAT_SMD_INTERFACE_DEDICATED:[interface_dedicated_footprint_expand, interface_dedicated_footprint_list_expand],
#   # CAT_SMD_INTERFACE_LIN_TRANSCEIVER:[interface_lin_transceiver_footprint_expand, interface_lin_transceiver_footprint_list_expand],
#   # CAT_SMD_INTERFACE_TELECOM:[interface_telecom_footprint_expand, interface_telecom_footprint_list_expand],
#   # CAT_SMD_ISOLATOR_CHIP:[isolator_chip_footprint_expand, isolator_chip_footprint_list_expand],
#   # CAT_SMD_JFET_JUNCTION_FIELD_EFFECT_TRANSISTOR:[jfet_junction_field_effect_transistor_footprint_expand, jfet_junction_field_effect_transistor_footprint_list_expand],
#   # CAT_SMD_LATCHES:[latches_footprint_expand, latches_footprint_list_expand],
#   # CAT_SMD_LCD_DRIVER:[lcd_driver_footprint_expand, lcd_driver_footprint_list_expand],
#   # CAT_SMD_LED_DRIVE:[led_drive_footprint_expand, led_drive_footprint_list_expand],
#   # CAT_SMD_LED_RESISTOR:[led_resistor_footprint_expand, led_resistor_footprint_list_expand],
#   # CAT_SMD_LED:[led_footprint_expand, led_footprint_list_expand],
#   # CAT_SMD_LEVEL_SHIFTER_SHIFTER:[level_shifter_shifter_footprint_expand, level_shifter_shifter_footprint_list_expand],
#   # CAT_SMD_LINEAR_VOLTAGE_REGULATOR_CHIP:[linear_voltage_regulator_chip_footprint_expand, linear_voltage_regulator_chip_footprint_list_expand],
#   # CAT_SMD_LOGIC_CHIP_:[logic_chip__footprint_expand, logic_chip__footprint_list_expand],
#   # CAT_SMD_LOGIC_CHIP_4000_SERIES:[logic_chip_4000_series_footprint_expand, logic_chip_4000_series_footprint_list_expand],
#   # CAT_SMD_LOGIC_CHIP_74_SERIES:[logic_chip_74_series_footprint_expand, logic_chip_74_series_footprint_list_expand],
#   # CAT_SMD_LOW_NOISE_OP_AMP:[low_noise_op_amp_footprint_expand, low_noise_op_amp_footprint_list_expand],
#   # CAT_SMD_LOW_POWER_OP_AMP:[low_power_op_amp_footprint_expand, low_power_op_amp_footprint_list_expand],
#   # CAT_SMD_LVDS_CHIP:[lvds_chip_footprint_expand, lvds_chip_footprint_list_expand],
#   # CAT_SMD_MAGNETIC_BEADS:[magnetic_beads_footprint_expand, magnetic_beads_footprint_list_expand],
#   # CAT_SMD_MAGNETIC_SENSOR:[magnetic_sensor_footprint_expand, magnetic_sensor_footprint_list_expand],
#   # CAT_SMD_MCU_MONITORING_CHIP:[mcu_monitoring_chip_footprint_expand, mcu_monitoring_chip_footprint_list_expand],
#   # CAT_SMD_MICROCONTROLLER_MCU:[microcontroller_mcu_footprint_expand, microcontroller_mcu_footprint_list_expand],
#   # CAT_SMD_MOS_DRIVE:[mos_drive_footprint_expand, mos_drive_footprint_list_expand],
#   # CAT_SMD_MOS_FIELD_EFFECT_TUBE:[mos_field_effect_tube_footprint_expand, mos_field_effect_tube_footprint_list_expand],
#   # CAT_SMD_MOTOR_DRIVER:[motor_driver_footprint_expand, motor_driver_footprint_list_expand],
#   # CAT_SMD_MULTI_FREQUENCY_OSCILLATOR:[multi_frequency_oscillator_footprint_expand, multi_frequency_oscillator_footprint_list_expand],
#   # CAT_SMD_NETWORK_PORT_TRANSFORMER:[network_port_transformer_footprint_expand, network_port_transformer_footprint_list_expand],
#   # CAT_SMD_NIOBIUM_OXIDE_CAPACITOR:[niobium_oxide_capacitor_footprint_expand, niobium_oxide_capacitor_footprint_list_expand],
#   # CAT_SMD_NTC_RESISTOR:[ntc_resistor_footprint_expand, ntc_resistor_footprint_list_expand],
#   # CAT_SMD_OP_AMP_GENERAL_OP_AMP:[op_amp_general_op_amp_footprint_expand, op_amp_general_op_amp_footprint_list_expand],
#   # CAT_SMD_OP_AMP_PRECISION_OP_AMP:[op_amp_precision_op_amp_footprint_expand, op_amp_precision_op_amp_footprint_list_expand],
#   # CAT_SMD_OPTICAL_SENSORS:[optical_sensors_footprint_expand, optical_sensors_footprint_list_expand],
#   # CAT_SMD_OPTOCOUPLER:[optocoupler_footprint_expand, optocoupler_footprint_list_expand],
#   # CAT_SMD_PASSIVE_CRYSTAL_RESONATOR:[passive_crystal_resonator_footprint_expand, passive_crystal_resonator_footprint_list_expand],
#   # CAT_SMD_PHOTOELECTRIC_SOLID_STATE_RELAY:[photoelectric_solid_state_relay_footprint_expand, photoelectric_solid_state_relay_footprint_list_expand],
#   # CAT_SMD_PHOTOELECTRIC_SWITCH:[photoelectric_switch_footprint_expand, photoelectric_switch_footprint_list_expand],
#   # CAT_SMD_PHOTOELECTRIC_TRIAC:[photoelectric_triac_footprint_expand, photoelectric_triac_footprint_list_expand],
#   # CAT_SMD_PORT_EXPANSION_CHIP:[port_expansion_chip_footprint_expand, port_expansion_chip_footprint_list_expand],
#   # CAT_SMD_POSITION_SENSOR:[position_sensor_footprint_expand, position_sensor_footprint_list_expand],
#   # CAT_SMD_POWER_INDUCTOR:[power_inductor_footprint_expand, power_inductor_footprint_list_expand],
#   # CAT_SMD_POWER_MONITORING_CHIP:[power_monitoring_chip_footprint_expand, power_monitoring_chip_footprint_list_expand],
#   # CAT_SMD_POWER_SWITCH_CHIP:[power_switch_chip_footprint_expand, power_switch_chip_footprint_list_expand],
#   # CAT_SMD_PRESSURE_SENSOR:[pressure_sensor_footprint_expand, pressure_sensor_footprint_list_expand],
#   # CAT_SMD_PROFESSIONAL_POWER_MANAGEMENT_PMIC:[professional_power_management_pmic_footprint_expand, professional_power_management_pmic_footprint_list_expand],
#   # CAT_SMD_PTC_RESETTABLE_FUSE:[ptc_resettable_fuse_footprint_expand, ptc_resettable_fuse_footprint_list_expand],
#   # CAT_SMD_REAL_TIME_CLOCK_CHIP:[real_time_clock_chip_footprint_expand, real_time_clock_chip_footprint_list_expand],
#   # CAT_SMD_RECTIFIER_BRIDGE:[rectifier_bridge_footprint_expand, rectifier_bridge_footprint_list_expand],
#   # CAT_SMD_RESISTOR_NETWORK:[resistor_network_footprint_expand, resistor_network_footprint_list_expand],
#   # CAT_SMD_RESISTOR:[resistor_footprint_expand, resistor_footprint_list_expand],
#   # CAT_SMD_RF_AMPLIFIER:[rf_amplifier_footprint_expand, rf_amplifier_footprint_list_expand],
#   # CAT_SMD_RF_ATTENUATOR:[rf_attenuator_footprint_expand, rf_attenuator_footprint_list_expand],
#   # CAT_SMD_RF_CARD_CHIP:[rf_card_chip_footprint_expand, rf_card_chip_footprint_list_expand],
#   # CAT_SMD_RF_COUPLER:[rf_coupler_footprint_expand, rf_coupler_footprint_list_expand],
#   # CAT_SMD_RF_DETECTOR:[rf_detector_footprint_expand, rf_detector_footprint_list_expand],
#   # CAT_SMD_RF_FILTER:[rf_filter_footprint_expand, rf_filter_footprint_list_expand],
#   # CAT_SMD_RF_MIXER:[rf_mixer_footprint_expand, rf_mixer_footprint_list_expand],
#   # CAT_SMD_RF_SWITCH:[rf_switch_footprint_expand, rf_switch_footprint_list_expand],
#   # CAT_SMD_RS232_CHIP:[rs232_chip_footprint_expand, rs232_chip_footprint_list_expand],
#   # CAT_SMD_RS485_RS422_CHIP:[rs485_rs422_chip_footprint_expand, rs485_rs422_chip_footprint_list_expand],
#   # CAT_SMD_SDRAM_MEMORY:[sdram_memory_footprint_expand, sdram_memory_footprint_list_expand],
#   # CAT_SMD_SECOND_CLASSIFICATION_OF_ENGINEERING_DEPARTMENT_DATA:[second_classification_of_engineering_department_data_footprint_expand, SECOND_CLASSIFICATION_OF_ENGINEERING_DEPARTMENT_DATA_footprint_list_expand],
#   # CAT_SMD_SECURITY_VERIFICATION_ENCRYPTION_CHIP:[security_verification_encryption_chip_footprint_expand, security_verification_encryption_chip_footprint_list_expand],
#   # CAT_SMD_SENSOR_INTERFACE_CHIP:[sensor_interface_chip_footprint_expand, sensor_interface_chip_footprint_list_expand],
#   # CAT_SMD_SERIAL_INTERFACE:[serial_interface_footprint_expand, serial_interface_footprint_list_expand],
#   # CAT_SMD_SHIFT_REGISTER:[shift_register_footprint_expand, shift_register_footprint_list_expand],
#   # CAT_SMD_SIGNAL_BUFFERS_REPEATERS_DISTRIBUTORS:[signal_buffers_repeaters_distributors_footprint_expand, signal_buffers_repeaters_distributors_footprint_list_expand],
#   # CAT_SMD_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS:[signal_switches_multiplexers_decoders_footprint_expand, signal_switches_multiplexers_decoders_footprint_list_expand],
#   # CAT_SMD_ACTIVE_CRYSTAL_OSCILLATOR:[smd_active_crystal_oscillator_footprint_expand, smd_active_crystal_oscillator_footprint_list_expand],
#   # CAT_SMD_SOLID_ELECTROLYTIC_CAPACITOR:[solid_electrolytic_capacitor_footprint_expand, solid_electrolytic_capacitor_footprint_list_expand],
#   # CAT_SMD_SOUND_SURFACE_RESONATOR_SAW:[sound_surface_resonator_saw_footprint_expand, sound_surface_resonator_saw_footprint_list_expand],
#   # CAT_SMD_SPECIAL_FUNCTION_AMPLIFIER:[special_function_amplifier_footprint_expand, special_function_amplifier_footprint_list_expand],
#   # CAT_SMD_SPECIAL_FUNCTION_DRIVEN:[special_function_driven_footprint_expand, special_function_driven_footprint_list_expand],
#   # CAT_SMD_SRAM_MEMORY:[sram_memory_footprint_expand, sram_memory_footprint_list_expand],
#   # CAT_SMD_SWITCHING_POWER_CHIP:[switching_power_chip_footprint_expand, switching_power_chip_footprint_list_expand],
#   # CAT_SMD_TACT_SWITCH:[tact_switch_footprint_expand, tact_switch_footprint_list_expand],
#   # CAT_SMD_TANTALUM_CAPACITOR:[tantalum_capacitor_footprint_expand, tantalum_capacitor_footprint_list_expand],
#   # CAT_SMD_TEMPERATURE_AND_HUMIDITY_SENSOR:[temperature_and_humidity_sensor_footprint_expand, temperature_and_humidity_sensor_footprint_list_expand],
#   # CAT_SMD_TEMPERATURE_SENSOR:[temperature_sensor_footprint_expand, temperature_sensor_footprint_list_expand],
#   # CAT_SMD_THYRISTOR:[thyristor_footprint_expand, thyristor_footprint_list_expand],
#   # CAT_SMD_TIME_BASE_INTEGRATED_CHIP:[time_base_integrated_chip_footprint_expand, time_base_integrated_chip_footprint_list_expand],
#   # CAT_SMD_TOUCH_CHIP:[touch_chip_footprint_expand, touch_chip_footprint_list_expand],
#   # CAT_SMD_TOUCH_SCREEN_CONTROLLER:[touch_screen_controller_footprint_expand, touch_screen_controller_footprint_list_expand],
#   # CAT_SMD_TRIGGER_DIODE:[trigger_diode_footprint_expand, trigger_diode_footprint_list_expand],
#   # CAT_SMD_TRIGGER:[trigger_footprint_expand, trigger_footprint_list_expand],
#   # CAT_SMD_TRIODE_DIGITAL_TRIODE:[triode_digital_triode_footprint_expand, triode_digital_triode_footprint_list_expand],
#   # CAT_SMD_TRIODE:[triode_footprint_expand, triode_footprint_list_expand],
#   # CAT_SMD_USB_CHIP:[usb_chip_footprint_expand, usb_chip_footprint_list_expand],
#   # CAT_SMD_VARICAP_DIODE:[varicap_diode_footprint_expand, varicap_diode_footprint_list_expand],
#   # CAT_SMD_VARISTOR:[varistor_footprint_expand, varistor_footprint_list_expand],
#   # CAT_SMD_VIDEO_AND_AUDIO_INTERFACE_CHIP:[video_and_audio_interface_chip_footprint_expand, video_and_audio_interface_chip_footprint_list_expand],
#   # CAT_SMD_VIDEO_FILTER_DRIVER:[video_filter_driver_footprint_expand, video_filter_driver_footprint_list_expand],
#   # CAT_SMD_VOLTAGE_COMPARATOR:[voltage_comparator_footprint_expand, voltage_comparator_footprint_list_expand],
#   # CAT_SMD_VOLTAGE_REFERENCE_CHIP:[voltage_reference_chip_footprint_expand, voltage_reference_chip_footprint_list_expand],
#   # CAT_SMD_WIRELESS_TRANSCEIVER_CHIP:[wireless_transceiver_chip_footprint_expand, wireless_transceiver_chip_footprint_list_expand],
#   CAT_SMD_LDO_LOW_DROPOUT_LINEAR_REGULATION:[ldo_low_dropout_linear_regulation_footprint_expand, ldo_low_dropout_linear_regulation_footprint_list_expand],

#   CAT_SMD_CAPACITOR: [capacitor_footprint_expand, capacitor_footprint_list_expand],
#   CAT_SMD_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_ESD_DIODE:   [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_HIGH_EFFICIENCY_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_INDUCTOR: [inductor_footprint_expand, inductor_footprint_list_expand],
#   CAT_SMD_LED: [led_footprint_expand, led_footprint_list_expand],
#   CAT_SMD_RESISTOR: [resistor_footprint_expand, resistor_footprint_list_expand],
#   CAT_SMD_SCHOTTKY_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_SWITCHING_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_TVS_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_ULTRA_FAST_RECOVERY_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
#   CAT_SMD_ZENER_DIODE: [diode_footprint_expand, diode_footprint_list_expand],
# }

def footprint_lookup(str_in, footprint_in):
  try:

    temp_dic =  footprint_in
    default_dic = default_footprint_expand

    # pprint(str_in)
    # pprint({**default_dic, **temp_dic}['0805'])
    # sys.exit()

    # NOTE: sequence is a concern, place most important at the end
    lookup_dic = {**default_dic, **temp_dic}

    return lookup_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_lookup', __file__)
    raise e
    sys.exit(1)

def footprint_list_lookup(str_in, footprint_list_in):
  try:
    temp_dic =  footprint_list_in
    default_dic = default_footprint_list_expand

    # NOTE: sequence is a concern, place most important at the end
    lookup_dic = {**default_dic, **temp_dic}

    return ' '+lookup_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_list_lookup', __file__)
    raise e
    sys.exit(1)
