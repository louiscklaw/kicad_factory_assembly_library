#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from footprint import *
from draw_symbol import *

master_table = [

  [CAT_SMD_CAPACITOR, 'output/sz_jlc_capacitor.lib', 'output/sz_jlc_capacitor.dcm', capacitor_footprint_expand, capacitor_footprint_list_expand, SMD_CAPACITOR_SYMBOL],

  [CAT_SMD_DIODE, 'output/sz_jlc_diode.lib', 'output/sz_jlc_diode.dcm', diode_footprint_expand, diode_footprint_list_expand, SMD_DIODE_SYMBOL],
  [CAT_SMD_ESD_DIODE,  'output/sz_jlc_esd_diode.lib', 'output/sz_jlc_esd_diode.dcm', diode_footprint_expand, diode_footprint_list_expand, SMD_DIODE_SYMBOL],
  [CAT_SMD_ZENER_DIODE,  'output/sz_jlc_zener_diode.lib', 'output/sz_jlc_zener_diode.dcm', diode_footprint_expand, diode_footprint_list_expand, SMD_DIODE_SYMBOL],
  [CAT_SMD_AVALANCHE_DIODE,  'output/sz_jlc_avalanche_diode.lib', 'output/sz_jlc_avalanche_diode.dcm', diode_footprint_expand, diode_footprint_list_expand, SMD_DIODE_SYMBOL],
  [CAT_SMD_LED, 'output/sz_jlc_led.lib', 'output/sz_jlc_led.dcm', diode_footprint_expand, diode_footprint_list_expand, SMD_LED_SYMBOL],

  [CAT_SMD_INDUCTOR, 'output/sz_jlc_inductor.lib', 'output/sz_jlc_inductor.dcm', inductor_footprint_expand, inductor_footprint_list_expand, SMD_INDUCTOR_SYMBOL],
  [CAT_SMD_RESISTOR, 'output/sz_jlc_resistor.lib', 'output/sz_jlc_resistor.dcm', resistor_footprint_expand, resistor_footprint_list_expand, SMD_RESISTOR_SYMBOL],
  [CAT_SMD_LDO_LOW_DROPOUT_LINEAR_REGULATION,  'output/sz_jlc_ldo_low_dropout_linear_regulation.lib', 'output/sz_jlc_ldo_low_dropout_linear_regulation.dcm', ldo_low_dropout_linear_regulation_footprint_expand, ldo_low_dropout_linear_regulation_footprint_list_expand, SMD_LDO_SYMBOL],

  # MCU
  # [CAT_SMD_MCU_MONITORING_CHIP,  'output/sz_jlc_mcu_monitoring_chip.lib', 'output/sz_jlc_mcu_monitoring_chip.dcm'],
  [CAT_SMD_MICROCONTROLLER_MCU,  'output/sz_jlc_microcontroller_mcu.lib', 'output/sz_jlc_microcontroller_mcu.dcm', microcontroller_mcu_footprint_expand, microcontroller_mcu_footprint_list_expand, SMD_MICROCONTROLLER_MCU_SYMBOL],

  [CAT_SMD_ACCELEROMETER,  'output/sz_jlc_accelerometer.lib', 'output/sz_jlc_accelerometer.dcm', accelerometer_footprint_expand, accelerometer_footprint_list_expand, SMD_ACCELEROMETER_SYMBOL],
  [CAT_SMD_ACTIVE_FILTER,  'output/sz_jlc_active_filter.lib', 'output/sz_jlc_active_filter.dcm', active_filter_footprint_expand, active_filter_footprint_list_expand, SMD_ACTIVE_FILTER_SYMBOL],
  [CAT_SMD_AMBIENT_LIGHT_SENSOR,  'output/sz_jlc_ambient_light_sensor.lib', 'output/sz_jlc_ambient_light_sensor.dcm', ambient_light_sensor_footprint_expand, ambient_light_sensor_footprint_list_expand, SMD_AMBIENT_LIGHT_SENSOR_SYMBOL],

  [CAT_SMD_AMPLIFIER,  'output/sz_jlc_amplifier.lib', 'output/sz_jlc_amplifier.dcm', amplifier_footprint_expand, amplifier_footprint_list_expand, SMD_AMPLIFIER_SYMBOL],
  [CAT_SMD_ACTIVE_CRYSTAL_OSCILLATOR,  'output/sz_jlc_active_crystal_oscillator.lib', 'output/sz_jlc_active_crystal_oscillator.dcm', active_crystal_oscillator_footprint_expand, active_crystal_oscillator_footprint_list_expand, SMD_ACTIVE_CRYSTAL_OSCILLATOR_SYMBOL],
  [CAT_SMD_ANALOG_SWITCH_CHIP,  'output/sz_jlc_analog_switch_chip.lib', 'output/sz_jlc_analog_switch_chip.dcm', analog_switch_chip_footprint_expand, analog_switch_chip_footprint_list_expand, SMD_ANALOG_SWITCH_CHIP_SYMBOL],
  [CAT_SMD_ANALOG_TO_DIGITAL_CONVERSION_CHIP,  'output/sz_jlc_analog_to_digital_conversion_chip.lib', 'output/sz_jlc_analog_to_digital_conversion_chip.dcm', analog_to_digital_conversion_chip_footprint_expand, analog_to_digital_conversion_chip_footprint_list_expand, SMD_ANALOG_TO_DIGITAL_CONVERSION_CHIP_SYMBOL],
  [CAT_SMD_ANGLE_SENSOR,  'output/sz_jlc_angle_sensor.lib', 'output/sz_jlc_angle_sensor.dcm', angle_sensor_footprint_expand, angle_sensor_footprint_list_expand, SMD_ANGLE_SENSOR_SYMBOL],
  [CAT_SMD_ANGULAR_VELOCITY_SENSOR,  'output/sz_jlc_angular_velocity_sensor.lib', 'output/sz_jlc_angular_velocity_sensor.dcm', angular_velocity_sensor_footprint_expand, angular_velocity_sensor_footprint_list_expand, SMD_ANGULAR_VELOCITY_SENSOR_SYMBOL],
  [CAT_SMD_ATTITUDE_SENSOR,  'output/sz_jlc_attitude_sensor.lib', 'output/sz_jlc_attitude_sensor.dcm', attitude_sensor_footprint_expand, attitude_sensor_footprint_list_expand, SMD_ATTITUDE_SENSOR_SYMBOL],
  [CAT_SMD_AUDIO_POWER_AMPLIFIER,  'output/sz_jlc_audio_power_amplifier.lib', 'output/sz_jlc_audio_power_amplifier.dcm', audio_power_amplifier_footprint_expand, audio_power_amplifier_footprint_list_expand, SMD_AUDIO_POWER_AMPLIFIER_SYMBOL],
  [CAT_SMD_BALANCED_UNBALANCED_TRANSFORMER,  'output/sz_jlc_balanced_unbalanced_transformer.lib', 'output/sz_jlc_balanced_unbalanced_transformer.dcm', balanced_unbalanced_transformer_footprint_expand, balanced_unbalanced_transformer_footprint_list_expand, SMD_BALANCED_UNBALANCED_TRANSFORMER_SYMBOL],
  [CAT_SMD_BALLAST_CONTROLLER,  'output/sz_jlc_ballast_controller.lib', 'output/sz_jlc_ballast_controller.dcm', ballast_controller_footprint_expand, ballast_controller_footprint_list_expand, SMD_BALLAST_CONTROLLER_SYMBOL],
  [CAT_SMD_BATTERY_BOX_BATTERY_HOLDER,  'output/sz_jlc_battery_box_battery_holder.lib', 'output/sz_jlc_battery_box_battery_holder.dcm', battery_box_battery_holder_footprint_expand, battery_box_battery_holder_footprint_list_expand, SMD_BATTERY_BOX_BATTERY_HOLDER_SYMBOL],
  [CAT_SMD_BATTERY_POWER_MANAGEMENT_CHIP,  'output/sz_jlc_battery_power_management_chip.lib', 'output/sz_jlc_battery_power_management_chip.dcm', battery_power_management_chip_footprint_expand, battery_power_management_chip_footprint_list_expand, SMD_BATTERY_POWER_MANAGEMENT_CHIP_SYMBOL],
  [CAT_SMD_BATTERY_PROTECTION_CHIP,  'output/sz_jlc_battery_protection_chip.lib', 'output/sz_jlc_battery_protection_chip.dcm', battery_protection_chip_footprint_expand, battery_protection_chip_footprint_list_expand, SMD_BATTERY_PROTECTION_CHIP_SYMBOL],
  [CAT_SMD_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS,  'output/sz_jlc_buffers_drivers_receivers_transceivers.lib', 'output/sz_jlc_buffers_drivers_receivers_transceivers.dcm', buffers_drivers_receivers_transceivers_footprint_expand, buffers_drivers_receivers_transceivers_footprint_list_expand, SMD_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS_SYMBOL],
  [CAT_SMD_CAN_CHIP,  'output/sz_jlc_can_chip.lib', 'output/sz_jlc_can_chip.dcm', can_chip_footprint_expand, can_chip_footprint_list_expand, SMD_CAN_CHIP_SYMBOL],
  [CAT_SMD_CERAMIC_RESONATOR,  'output/sz_jlc_ceramic_resonator.lib', 'output/sz_jlc_ceramic_resonator.dcm', ceramic_resonator_footprint_expand, ceramic_resonator_footprint_list_expand, SMD_CERAMIC_RESONATOR_SYMBOL],
  [CAT_SMD_CLOCK_BUFFER_DRIVER,  'output/sz_jlc_clock_buffer_driver.lib', 'output/sz_jlc_clock_buffer_driver.dcm', clock_buffer_driver_footprint_expand, clock_buffer_driver_footprint_list_expand, SMD_CLOCK_BUFFER_DRIVER_SYMBOL],
  [CAT_SMD_CLOCK_GENERATOR_PLL_FREQUENCY_SYNTHESIZER,  'output/sz_jlc_clock_generator_pll_frequency_synthesizer.lib', 'output/sz_jlc_clock_generator_pll_frequency_synthesizer.dcm', clock_generator_pll_frequency_synthesizer_footprint_expand, clock_generator_pll_frequency_synthesizer_footprint_list_expand, SMD_CLOCK_GENERATOR_PLL_FREQUENCY_SYNTHESIZER_SYMBOL],
  [CAT_SMD_CLOCK_TIMING_DEDICATED,  'output/sz_jlc_clock_timing_dedicated.lib', 'output/sz_jlc_clock_timing_dedicated.dcm', clock_timing_dedicated_footprint_expand, clock_timing_dedicated_footprint_list_expand, SMD_CLOCK_TIMING_DEDICATED_SYMBOL],
  [CAT_SMD_CODEC_CHIP,  'output/sz_jlc_codec_chip.lib', 'output/sz_jlc_codec_chip.dcm', codec_chip_footprint_expand, codec_chip_footprint_list_expand, SMD_CODEC_CHIP_SYMBOL],
  [CAT_SMD_COLOR_SENSOR,  'output/sz_jlc_color_sensor.lib', 'output/sz_jlc_color_sensor.dcm', color_sensor_footprint_expand, color_sensor_footprint_list_expand, SMD_COLOR_SENSOR_SYMBOL],
  [CAT_SMD_COMMON_MODE_INDUCTOR_FILTER,  'output/sz_jlc_common_mode_inductor_filter.lib', 'output/sz_jlc_common_mode_inductor_filter.dcm', common_mode_inductor_filter_footprint_expand, common_mode_inductor_filter_footprint_list_expand, SMD_COMMON_MODE_INDUCTOR_FILTER_SYMBOL],
  [CAT_SMD_CONSTANT_CURRENT_DIODE,  'output/sz_jlc_constant_current_diode.lib', 'output/sz_jlc_constant_current_diode.dcm', constant_current_diode_footprint_expand, constant_current_diode_footprint_list_expand, SMD_CONSTANT_CURRENT_DIODE_SYMBOL],
  [CAT_SMD_CONSTANT_CURRENT_DIODE,  'output/sz_jlc_constant_current_diode.lib', 'output/sz_jlc_constant_current_diode.dcm', constant_current_diode_footprint_expand, constant_current_diode_footprint_list_expand, SMD_CONSTANT_CURRENT_DIODE_SYMBOL],
  [CAT_SMD_COUNTER_DIVIDER,  'output/sz_jlc_counter_divider.lib', 'output/sz_jlc_counter_divider.dcm', counter_divider_footprint_expand, counter_divider_footprint_list_expand, SMD_COUNTER_DIVIDER_SYMBOL],
  [CAT_SMD_CPLD_FPGA_CHIP,  'output/sz_jlc_cpld_fpga_chip.lib', 'output/sz_jlc_cpld_fpga_chip.dcm', cpld_fpga_chip_footprint_expand, cpld_fpga_chip_footprint_list_expand, SMD_CPLD_FPGA_CHIP_SYMBOL],
  [CAT_SMD_CURRENT_MONITORING_CHIP,  'output/sz_jlc_current_monitoring_chip.lib', 'output/sz_jlc_current_monitoring_chip.dcm', current_monitoring_chip_footprint_expand, current_monitoring_chip_footprint_list_expand, SMD_CURRENT_MONITORING_CHIP_SYMBOL],
  [CAT_SMD_CURRENT_SENSOR,  'output/sz_jlc_current_sensor.lib', 'output/sz_jlc_current_sensor.dcm', current_sensor_footprint_expand, current_sensor_footprint_list_expand, SMD_CURRENT_SENSOR_SYMBOL],
  [CAT_SMD_DARLINGTON_TRANSISTOR_ARRAY_DRIVE,  'output/sz_jlc_darlington_transistor_array_drive.lib', 'output/sz_jlc_darlington_transistor_array_drive.dcm', darlington_transistor_array_drive_footprint_expand, darlington_transistor_array_drive_footprint_list_expand, SMD_DARLINGTON_TRANSISTOR_ARRAY_DRIVE_SYMBOL],
  [CAT_SMD_DARLINGTON,  'output/sz_jlc_darlington.lib', 'output/sz_jlc_darlington.dcm', darlington_footprint_expand, darlington_footprint_list_expand, SMD_DARLINGTON_SYMBOL],
  [CAT_SMD_DC_DC_CHIP,  'output/sz_jlc_dc_dc_chip.lib', 'output/sz_jlc_dc_dc_chip.dcm', dc_dc_chip_footprint_expand, dc_dc_chip_footprint_list_expand, SMD_DC_DC_CHIP_SYMBOL],
  [CAT_SMD_DDR_MEMORY,  'output/sz_jlc_ddr_memory.lib', 'output/sz_jlc_ddr_memory.dcm', ddr_memory_footprint_expand, ddr_memory_footprint_list_expand, SMD_DDR_MEMORY_SYMBOL],
  [CAT_SMD_DDS_CHIP,  'output/sz_jlc_dds_chip.lib', 'output/sz_jlc_dds_chip.dcm', dds_chip_footprint_expand, dds_chip_footprint_list_expand, SMD_DDS_CHIP_SYMBOL],
  [CAT_SMD_DEDICATED_SENSORS,  'output/sz_jlc_dedicated_sensors.lib', 'output/sz_jlc_dedicated_sensors.dcm', dedicated_sensors_footprint_expand, dedicated_sensors_footprint_list_expand, SMD_DEDICATED_SENSORS_SYMBOL],
  [CAT_SMD_DIFFERENTIAL_OP_AMPS,  'output/sz_jlc_differential_op_amps.lib', 'output/sz_jlc_differential_op_amps.dcm', differential_op_amps_footprint_expand, differential_op_amps_footprint_list_expand, SMD_DIFFERENTIAL_OP_AMPS_SYMBOL],
  [CAT_SMD_DIGITAL_POTENTIOMETER_CHIP,  'output/sz_jlc_digital_potentiometer_chip.lib', 'output/sz_jlc_digital_potentiometer_chip.dcm', digital_potentiometer_chip_footprint_expand, digital_potentiometer_chip_footprint_list_expand, SMD_DIGITAL_POTENTIOMETER_CHIP_SYMBOL],
  [CAT_SMD_DIGITAL_TO_ANALOG_CONVERSION_CHIP,  'output/sz_jlc_digital_to_analog_conversion_chip.lib', 'output/sz_jlc_digital_to_analog_conversion_chip.dcm', digital_to_analog_conversion_chip_footprint_expand, digital_to_analog_conversion_chip_footprint_list_expand, SMD_DIGITAL_TO_ANALOG_CONVERSION_CHIP_SYMBOL],
  [CAT_SMD_DISCHARGE_TUBE,  'output/sz_jlc_discharge_tube.lib', 'output/sz_jlc_discharge_tube.dcm', discharge_tube_footprint_expand, discharge_tube_footprint_list_expand, SMD_DISCHARGE_TUBE_SYMBOL],
  [CAT_SMD_DISPOSABLE_FUSES,  'output/sz_jlc_disposable_fuses.lib', 'output/sz_jlc_disposable_fuses.dcm', disposable_fuses_footprint_expand, disposable_fuses_footprint_list_expand, SMD_DISPOSABLE_FUSES_SYMBOL],
  [CAT_SMD_DRIVER_CHIP,  'output/sz_jlc_driver_chip.lib', 'output/sz_jlc_driver_chip.dcm', driver_chip_footprint_expand, driver_chip_footprint_list_expand, SMD_DRIVER_CHIP_SYMBOL],
  [CAT_SMD_EEPROM_MEMORY,  'output/sz_jlc_eeprom_memory.lib', 'output/sz_jlc_eeprom_memory.dcm', eeprom_memory_footprint_expand, eeprom_memory_footprint_list_expand, SMD_EEPROM_MEMORY_SYMBOL],
  [CAT_SMD_EL_DRIVE,  'output/sz_jlc_el_drive.lib', 'output/sz_jlc_el_drive.dcm', el_drive_footprint_expand, el_drive_footprint_list_expand, SMD_EL_DRIVE_SYMBOL],
  [CAT_SMD_ELECTROLYTIC_CAPACITORS,  'output/sz_jlc_electrolytic_capacitors.lib', 'output/sz_jlc_electrolytic_capacitors.dcm', electrolytic_capacitors_footprint_expand, electrolytic_capacitors_footprint_list_expand, SMD_ELECTROLYTIC_CAPACITORS_SYMBOL],
  [CAT_SMD_EMI_RFI_FILTERS_LC_RC_NETWORKS,  'output/sz_jlc_emi_rfi_filters_lc_rc_networks.lib', 'output/sz_jlc_emi_rfi_filters_lc_rc_networks.dcm', emi_rfi_filters_lc_rc_networks_footprint_expand, emi_rfi_filters_lc_rc_networks_footprint_list_expand, SMD_EMI_RFI_FILTERS_LC_RC_NETWORKS_SYMBOL],
  [CAT_SMD_EPROM_MEMORY,  'output/sz_jlc_eprom_memory.lib', 'output/sz_jlc_eprom_memory.dcm', eprom_memory_footprint_expand, eprom_memory_footprint_list_expand, SMD_EPROM_MEMORY_SYMBOL],
  [CAT_SMD_ETHERNET_CHIP,  'output/sz_jlc_ethernet_chip.lib', 'output/sz_jlc_ethernet_chip.dcm', ethernet_chip_footprint_expand, ethernet_chip_footprint_list_expand, SMD_ETHERNET_CHIP_SYMBOL],
  [CAT_SMD_FAST_RECOVERY_DIODE,  'output/sz_jlc_fast_recovery_diode.lib', 'output/sz_jlc_fast_recovery_diode.dcm', fast_recovery_diode_footprint_expand, fast_recovery_diode_footprint_list_expand, SMD_FAST_RECOVERY_DIODE_SYMBOL],
  [CAT_SMD_FAST_RECOVERY_DIODE,  'output/sz_jlc_fast_recovery_diode.lib', 'output/sz_jlc_fast_recovery_diode.dcm', fast_recovery_diode_footprint_expand, fast_recovery_diode_footprint_list_expand, SMD_FAST_RECOVERY_DIODE_SYMBOL],
  [CAT_SMD_FET_INPUT_OP_AMP,  'output/sz_jlc_fet_input_op_amp.lib', 'output/sz_jlc_fet_input_op_amp.dcm', fet_input_op_amp_footprint_expand, fet_input_op_amp_footprint_list_expand, SMD_FET_INPUT_OP_AMP_SYMBOL],
  [CAT_SMD_FLASH_MEMORY,  'output/sz_jlc_flash_memory.lib', 'output/sz_jlc_flash_memory.dcm', flash_memory_footprint_expand, flash_memory_footprint_list_expand, SMD_FLASH_MEMORY_SYMBOL],
  [CAT_SMD_FONT_CHIP,  'output/sz_jlc_font_chip.lib', 'output/sz_jlc_font_chip.dcm', font_chip_footprint_expand, font_chip_footprint_list_expand, SMD_FONT_CHIP_SYMBOL],
  [CAT_SMD_FRAM_MEMORY,  'output/sz_jlc_fram_memory.lib', 'output/sz_jlc_fram_memory.dcm', fram_memory_footprint_expand, fram_memory_footprint_list_expand, SMD_FRAM_MEMORY_SYMBOL],
  [CAT_SMD_FUEL_GAUGE_CHIP,  'output/sz_jlc_fuel_gauge_chip.lib', 'output/sz_jlc_fuel_gauge_chip.dcm', fuel_gauge_chip_footprint_expand, fuel_gauge_chip_footprint_list_expand, SMD_FUEL_GAUGE_CHIP_SYMBOL],
  [CAT_SMD_FULL_BRIDGE_HALF_BRIDGE_DRIVE,  'output/sz_jlc_full_bridge_half_bridge_drive.lib', 'output/sz_jlc_full_bridge_half_bridge_drive.dcm', full_bridge_half_bridge_drive_footprint_expand, full_bridge_half_bridge_drive_footprint_list_expand, SMD_FULL_BRIDGE_HALF_BRIDGE_DRIVE_SYMBOL],
  [CAT_SMD_GAS_SENSOR,  'output/sz_jlc_gas_sensor.lib', 'output/sz_jlc_gas_sensor.dcm', gas_sensor_footprint_expand, gas_sensor_footprint_list_expand, SMD_GAS_SENSOR_SYMBOL],
  [CAT_SMD_GATE_AND_INVERTER,  'output/sz_jlc_gate_and_inverter.lib', 'output/sz_jlc_gate_and_inverter.dcm', gate_and_inverter_footprint_expand, gate_and_inverter_footprint_list_expand, SMD_GATE_AND_INVERTER_SYMBOL],
  [CAT_SMD_HF_INDUCTOR,  'output/sz_jlc_hf_inductor.lib', 'output/sz_jlc_hf_inductor.dcm', hf_inductor_footprint_expand, hf_inductor_footprint_list_expand, SMD_HF_INDUCTOR_SYMBOL],
  [CAT_SMD_HIGH_EFFICIENCY_DIODE,  'output/sz_jlc_high_efficiency_diode.lib', 'output/sz_jlc_high_efficiency_diode.dcm', high_efficiency_diode_footprint_expand, high_efficiency_diode_footprint_list_expand, SMD_HIGH_EFFICIENCY_DIODE_SYMBOL],
  [CAT_SMD_HIGH_PRESISION_RESISTOR,  'output/sz_jlc_high_presision_resistor.lib', 'output/sz_jlc_high_presision_resistor.dcm', high_presision_resistor_footprint_expand, high_presision_resistor_footprint_list_expand, SMD_HIGH_PRESISION_RESISTOR_SYMBOL],
  [CAT_SMD_HIGH_SPEED_BROADBAND_OP_AMP,  'output/sz_jlc_high_speed_broadband_op_amp.lib', 'output/sz_jlc_high_speed_broadband_op_amp.dcm', high_speed_broadband_op_amp_footprint_expand, high_speed_broadband_op_amp_footprint_list_expand, SMD_HIGH_SPEED_BROADBAND_OP_AMP_SYMBOL],
  [CAT_SMD_HIGH_VOLTAGE_RESISTOR,  'output/sz_jlc_high_voltage_resistor.lib', 'output/sz_jlc_high_voltage_resistor.dcm', high_voltage_resistor_footprint_expand, high_voltage_resistor_footprint_list_expand, SMD_HIGH_VOLTAGE_RESISTOR_SYMBOL],
  [CAT_SMD_I_O_EXPANDER,  'output/sz_jlc_i_o_expander.lib', 'output/sz_jlc_i_o_expander.dcm', i_o_expander_footprint_expand, i_o_expander_footprint_list_expand, SMD_I_O_EXPANDER_SYMBOL],
  [CAT_SMD_IGBT_DRIVE,  'output/sz_jlc_igbt_drive.lib', 'output/sz_jlc_igbt_drive.dcm', igbt_drive_footprint_expand, igbt_drive_footprint_list_expand, SMD_IGBT_DRIVE_SYMBOL],
  [CAT_SMD_IGBT_TUBE,  'output/sz_jlc_igbt_tube.lib', 'output/sz_jlc_igbt_tube.dcm', igbt_tube_footprint_expand, igbt_tube_footprint_list_expand, SMD_IGBT_TUBE_SYMBOL],
  [CAT_SMD_INFRARED_EMISSION_TUBE,  'output/sz_jlc_infrared_emission_tube.lib', 'output/sz_jlc_infrared_emission_tube.dcm', infrared_emission_tube_footprint_expand, infrared_emission_tube_footprint_list_expand, SMD_INFRARED_EMISSION_TUBE_SYMBOL],
  [CAT_SMD_INFRARED_RECEIVER_TUBE,  'output/sz_jlc_infrared_receiver_tube.lib', 'output/sz_jlc_infrared_receiver_tube.dcm', infrared_receiver_tube_footprint_expand, infrared_receiver_tube_footprint_list_expand, SMD_INFRARED_RECEIVER_TUBE_SYMBOL],
  [CAT_SMD_INFRARED_SENSOR,  'output/sz_jlc_infrared_sensor.lib', 'output/sz_jlc_infrared_sensor.dcm', infrared_sensor_footprint_expand, infrared_sensor_footprint_list_expand, SMD_INFRARED_SENSOR_SYMBOL],
  [CAT_SMD_INSTRUMENT_OPERATIONAL_AMPLIFIER,  'output/sz_jlc_instrument_operational_amplifier.lib', 'output/sz_jlc_instrument_operational_amplifier.dcm', instrument_operational_amplifier_footprint_expand, instrument_operational_amplifier_footprint_list_expand, SMD_INSTRUMENT_OPERATIONAL_AMPLIFIER_SYMBOL],
  [CAT_SMD_INTERFACE_CHIP,  'output/sz_jlc_interface_chip.lib', 'output/sz_jlc_interface_chip.dcm', interface_chip_footprint_expand, interface_chip_footprint_list_expand, SMD_INTERFACE_CHIP_SYMBOL],
  [CAT_SMD_INTERFACE_CONTROLLER,  'output/sz_jlc_interface_controller.lib', 'output/sz_jlc_interface_controller.dcm', interface_controller_footprint_expand, interface_controller_footprint_list_expand, SMD_INTERFACE_CONTROLLER_SYMBOL],
  [CAT_SMD_INTERFACE_DEDICATED,  'output/sz_jlc_interface_dedicated.lib', 'output/sz_jlc_interface_dedicated.dcm', interface_dedicated_footprint_expand, interface_dedicated_footprint_list_expand, SMD_INTERFACE_DEDICATED_SYMBOL],
  [CAT_SMD_INTERFACE_LIN_TRANSCEIVER,  'output/sz_jlc_interface_lin_transceiver.lib', 'output/sz_jlc_interface_lin_transceiver.dcm', interface_lin_transceiver_footprint_expand, interface_lin_transceiver_footprint_list_expand, SMD_INTERFACE_LIN_TRANSCEIVER_SYMBOL],
  [CAT_SMD_INTERFACE_TELECOM,  'output/sz_jlc_interface_telecom.lib', 'output/sz_jlc_interface_telecom.dcm', interface_telecom_footprint_expand, interface_telecom_footprint_list_expand, SMD_INTERFACE_TELECOM_SYMBOL],
  [CAT_SMD_ISOLATOR_CHIP,  'output/sz_jlc_isolator_chip.lib', 'output/sz_jlc_isolator_chip.dcm', isolator_chip_footprint_expand, isolator_chip_footprint_list_expand, SMD_ISOLATOR_CHIP_SYMBOL],
  [CAT_SMD_JFET_JUNCTION_FIELD_EFFECT_TRANSISTOR,  'output/sz_jlc_jfet_junction_field_effect_transistor.lib', 'output/sz_jlc_jfet_junction_field_effect_transistor.dcm', jfet_junction_field_effect_transistor_footprint_expand, jfet_junction_field_effect_transistor_footprint_list_expand, SMD_JFET_JUNCTION_FIELD_EFFECT_TRANSISTOR_SYMBOL],
  [CAT_SMD_LATCHES,  'output/sz_jlc_latches.lib', 'output/sz_jlc_latches.dcm', latches_footprint_expand, latches_footprint_list_expand, SMD_LATCHES_SYMBOL],
  [CAT_SMD_LCD_DRIVER,  'output/sz_jlc_lcd_driver.lib', 'output/sz_jlc_lcd_driver.dcm', lcd_driver_footprint_expand, lcd_driver_footprint_list_expand, SMD_LCD_DRIVER_SYMBOL],
  [CAT_SMD_LEVEL_SHIFTER_SHIFTER,  'output/sz_jlc_level_shifter_shifter.lib', 'output/sz_jlc_level_shifter_shifter.dcm', level_shifter_shifter_footprint_expand, level_shifter_shifter_footprint_list_expand, SMD_LEVEL_SHIFTER_SHIFTER_SYMBOL],
  [CAT_SMD_LINEAR_VOLTAGE_REGULATOR_CHIP,  'output/sz_jlc_linear_voltage_regulator_chip.lib', 'output/sz_jlc_linear_voltage_regulator_chip.dcm', linear_voltage_regulator_chip_footprint_expand, linear_voltage_regulator_chip_footprint_list_expand, SMD_LINEAR_VOLTAGE_REGULATOR_CHIP_SYMBOL],
  [CAT_SMD_LOGIC_CHIP_,  'output/sz_jlc_logic_chip_.lib', 'output/sz_jlc_logic_chip_.dcm', logic_chip__footprint_expand, logic_chip__footprint_list_expand, SMD_LOGIC_CHIP__SYMBOL],
  [CAT_SMD_LOGIC_CHIP_4000_SERIES,  'output/sz_jlc_logic_chip_4000_series.lib', 'output/sz_jlc_logic_chip_4000_series.dcm', logic_chip_4000_series_footprint_expand, logic_chip_4000_series_footprint_list_expand, SMD_LOGIC_CHIP_4000_SERIES_SYMBOL],
  [CAT_SMD_LOGIC_CHIP_74_SERIES,  'output/sz_jlc_logic_chip_74_series.lib', 'output/sz_jlc_logic_chip_74_series.dcm', logic_chip_74_series_footprint_expand, logic_chip_74_series_footprint_list_expand, SMD_LOGIC_CHIP_74_SERIES_SYMBOL],
  [CAT_SMD_LOW_NOISE_OP_AMP,  'output/sz_jlc_low_noise_op_amp.lib', 'output/sz_jlc_low_noise_op_amp.dcm', low_noise_op_amp_footprint_expand, low_noise_op_amp_footprint_list_expand, SMD_LOW_NOISE_OP_AMP_SYMBOL],
  [CAT_SMD_LOW_POWER_OP_AMP,  'output/sz_jlc_low_power_op_amp.lib', 'output/sz_jlc_low_power_op_amp.dcm', low_power_op_amp_footprint_expand, low_power_op_amp_footprint_list_expand, SMD_LOW_POWER_OP_AMP_SYMBOL],
  [CAT_SMD_LVDS_CHIP,  'output/sz_jlc_lvds_chip.lib', 'output/sz_jlc_lvds_chip.dcm', lvds_chip_footprint_expand, lvds_chip_footprint_list_expand, SMD_LVDS_CHIP_SYMBOL],
  [CAT_SMD_MAGNETIC_BEADS,  'output/sz_jlc_magnetic_beads.lib', 'output/sz_jlc_magnetic_beads.dcm', magnetic_beads_footprint_expand, magnetic_beads_footprint_list_expand, SMD_MAGNETIC_BEADS_SYMBOL],
  [CAT_SMD_MAGNETIC_SENSOR,  'output/sz_jlc_magnetic_sensor.lib', 'output/sz_jlc_magnetic_sensor.dcm', magnetic_sensor_footprint_expand, magnetic_sensor_footprint_list_expand, SMD_MAGNETIC_SENSOR_SYMBOL],
  [CAT_SMD_MOS_DRIVE,  'output/sz_jlc_mos_drive.lib', 'output/sz_jlc_mos_drive.dcm', mos_drive_footprint_expand, mos_drive_footprint_list_expand, SMD_MOS_DRIVE_SYMBOL],
  [CAT_SMD_MOS_FIELD_EFFECT_TUBE,  'output/sz_jlc_mos_field_effect_tube.lib', 'output/sz_jlc_mos_field_effect_tube.dcm', mos_field_effect_tube_footprint_expand, mos_field_effect_tube_footprint_list_expand, SMD_MOS_FIELD_EFFECT_TUBE_SYMBOL],
  [CAT_SMD_MOTOR_DRIVER,  'output/sz_jlc_motor_driver.lib', 'output/sz_jlc_motor_driver.dcm', motor_driver_footprint_expand, motor_driver_footprint_list_expand, SMD_MOTOR_DRIVER_SYMBOL],
  [CAT_SMD_MULTI_FREQUENCY_OSCILLATOR,  'output/sz_jlc_multi_frequency_oscillator.lib', 'output/sz_jlc_multi_frequency_oscillator.dcm', multi_frequency_oscillator_footprint_expand, multi_frequency_oscillator_footprint_list_expand, SMD_MULTI_FREQUENCY_OSCILLATOR_SYMBOL],
  [CAT_SMD_NETWORK_PORT_TRANSFORMER,  'output/sz_jlc_network_port_transformer.lib', 'output/sz_jlc_network_port_transformer.dcm', network_port_transformer_footprint_expand, network_port_transformer_footprint_list_expand, SMD_NETWORK_PORT_TRANSFORMER_SYMBOL],
  [CAT_SMD_NIOBIUM_OXIDE_CAPACITOR,  'output/sz_jlc_niobium_oxide_capacitor.lib', 'output/sz_jlc_niobium_oxide_capacitor.dcm', niobium_oxide_capacitor_footprint_expand, niobium_oxide_capacitor_footprint_list_expand, SMD_NIOBIUM_OXIDE_CAPACITOR_SYMBOL],
  [CAT_SMD_NTC_RESISTOR,  'output/sz_jlc_ntc_resistor.lib', 'output/sz_jlc_ntc_resistor.dcm', ntc_resistor_footprint_expand, ntc_resistor_footprint_list_expand, SMD_NTC_RESISTOR_SYMBOL],
  [CAT_SMD_OP_AMP_GENERAL_OP_AMP,  'output/sz_jlc_op_amp_general_op_amp.lib', 'output/sz_jlc_op_amp_general_op_amp.dcm', op_amp_general_op_amp_footprint_expand, op_amp_general_op_amp_footprint_list_expand, SMD_OP_AMP_GENERAL_OP_AMP_SYMBOL],
  [CAT_SMD_OP_AMP_PRECISION_OP_AMP,  'output/sz_jlc_op_amp_precision_op_amp.lib', 'output/sz_jlc_op_amp_precision_op_amp.dcm', op_amp_precision_op_amp_footprint_expand, op_amp_precision_op_amp_footprint_list_expand, SMD_OP_AMP_PRECISION_OP_AMP_SYMBOL],
  [CAT_SMD_OPTICAL_SENSORS,  'output/sz_jlc_optical_sensors.lib', 'output/sz_jlc_optical_sensors.dcm', optical_sensors_footprint_expand, optical_sensors_footprint_list_expand, SMD_OPTICAL_SENSORS_SYMBOL],
  [CAT_SMD_OPTOCOUPLER,  'output/sz_jlc_optocoupler.lib', 'output/sz_jlc_optocoupler.dcm', optocoupler_footprint_expand, optocoupler_footprint_list_expand, SMD_OPTOCOUPLER_SYMBOL],
  [CAT_SMD_PASSIVE_CRYSTAL_RESONATOR,  'output/sz_jlc_passive_crystal_resonator.lib', 'output/sz_jlc_passive_crystal_resonator.dcm', passive_crystal_resonator_footprint_expand, passive_crystal_resonator_footprint_list_expand, SMD_PASSIVE_CRYSTAL_RESONATOR_SYMBOL],
  [CAT_SMD_PHOTOELECTRIC_SOLID_STATE_RELAY,  'output/sz_jlc_photoelectric_solid_state_relay.lib', 'output/sz_jlc_photoelectric_solid_state_relay.dcm', photoelectric_solid_state_relay_footprint_expand, photoelectric_solid_state_relay_footprint_list_expand, SMD_PHOTOELECTRIC_SOLID_STATE_RELAY_SYMBOL],
  [CAT_SMD_PHOTOELECTRIC_SWITCH,  'output/sz_jlc_photoelectric_switch.lib', 'output/sz_jlc_photoelectric_switch.dcm', photoelectric_switch_footprint_expand, photoelectric_switch_footprint_list_expand, SMD_PHOTOELECTRIC_SWITCH_SYMBOL],
  [CAT_SMD_PHOTOELECTRIC_TRIAC,  'output/sz_jlc_photoelectric_triac.lib', 'output/sz_jlc_photoelectric_triac.dcm', photoelectric_triac_footprint_expand, photoelectric_triac_footprint_list_expand, SMD_PHOTOELECTRIC_TRIAC_SYMBOL],
  [CAT_SMD_PORT_EXPANSION_CHIP,  'output/sz_jlc_port_expansion_chip.lib', 'output/sz_jlc_port_expansion_chip.dcm', port_expansion_chip_footprint_expand, port_expansion_chip_footprint_list_expand, SMD_PORT_EXPANSION_CHIP_SYMBOL],
  [CAT_SMD_POSITION_SENSOR,  'output/sz_jlc_position_sensor.lib', 'output/sz_jlc_position_sensor.dcm', position_sensor_footprint_expand, position_sensor_footprint_list_expand, SMD_POSITION_SENSOR_SYMBOL],
  [CAT_SMD_POWER_INDUCTOR,  'output/sz_jlc_power_inductor.lib', 'output/sz_jlc_power_inductor.dcm', power_inductor_footprint_expand, power_inductor_footprint_list_expand, SMD_POWER_INDUCTOR_SYMBOL],
  [CAT_SMD_POWER_MONITORING_CHIP,  'output/sz_jlc_power_monitoring_chip.lib', 'output/sz_jlc_power_monitoring_chip.dcm', power_monitoring_chip_footprint_expand, power_monitoring_chip_footprint_list_expand, SMD_POWER_MONITORING_CHIP_SYMBOL],
  [CAT_SMD_POWER_SWITCH_CHIP,  'output/sz_jlc_power_switch_chip.lib', 'output/sz_jlc_power_switch_chip.dcm', power_switch_chip_footprint_expand, power_switch_chip_footprint_list_expand, SMD_POWER_SWITCH_CHIP_SYMBOL],
  [CAT_SMD_PRESSURE_SENSOR,  'output/sz_jlc_pressure_sensor.lib', 'output/sz_jlc_pressure_sensor.dcm', pressure_sensor_footprint_expand, pressure_sensor_footprint_list_expand, SMD_PRESSURE_SENSOR_SYMBOL],
  [CAT_SMD_PROFESSIONAL_POWER_MANAGEMENT_PMIC,  'output/sz_jlc_professional_power_management_pmic.lib', 'output/sz_jlc_professional_power_management_pmic.dcm', professional_power_management_pmic_footprint_expand, professional_power_management_pmic_footprint_list_expand, SMD_PROFESSIONAL_POWER_MANAGEMENT_PMIC_SYMBOL],
  [CAT_SMD_PTC_RESETTABLE_FUSE,  'output/sz_jlc_ptc_resettable_fuse.lib', 'output/sz_jlc_ptc_resettable_fuse.dcm', ptc_resettable_fuse_footprint_expand, ptc_resettable_fuse_footprint_list_expand, SMD_PTC_RESETTABLE_FUSE_SYMBOL],
  [CAT_SMD_REAL_TIME_CLOCK_CHIP,  'output/sz_jlc_real_time_clock_chip.lib', 'output/sz_jlc_real_time_clock_chip.dcm', real_time_clock_chip_footprint_expand, real_time_clock_chip_footprint_list_expand, SMD_REAL_TIME_CLOCK_CHIP_SYMBOL],
  [CAT_SMD_RECTIFIER_BRIDGE,  'output/sz_jlc_rectifier_bridge.lib', 'output/sz_jlc_rectifier_bridge.dcm', rectifier_bridge_footprint_expand, rectifier_bridge_footprint_list_expand, SMD_RECTIFIER_BRIDGE_SYMBOL],
  [CAT_SMD_RESISTOR_NETWORK,  'output/sz_jlc_resistor_network.lib', 'output/sz_jlc_resistor_network.dcm', resistor_network_footprint_expand, resistor_network_footprint_list_expand, SMD_RESISTOR_NETWORK_SYMBOL],
  [CAT_SMD_RF_AMPLIFIER,  'output/sz_jlc_rf_amplifier.lib', 'output/sz_jlc_rf_amplifier.dcm', rf_amplifier_footprint_expand, rf_amplifier_footprint_list_expand, SMD_RF_AMPLIFIER_SYMBOL],
  [CAT_SMD_RF_ATTENUATOR,  'output/sz_jlc_rf_attenuator.lib', 'output/sz_jlc_rf_attenuator.dcm', rf_attenuator_footprint_expand, rf_attenuator_footprint_list_expand, SMD_RF_ATTENUATOR_SYMBOL],
  [CAT_SMD_RF_CARD_CHIP,  'output/sz_jlc_rf_card_chip.lib', 'output/sz_jlc_rf_card_chip.dcm', rf_card_chip_footprint_expand, rf_card_chip_footprint_list_expand, SMD_RF_CARD_CHIP_SYMBOL],
  [CAT_SMD_RF_COUPLER,  'output/sz_jlc_rf_coupler.lib', 'output/sz_jlc_rf_coupler.dcm', rf_coupler_footprint_expand, rf_coupler_footprint_list_expand, SMD_RF_COUPLER_SYMBOL],
  [CAT_SMD_RF_DETECTOR,  'output/sz_jlc_rf_detector.lib', 'output/sz_jlc_rf_detector.dcm', rf_detector_footprint_expand, rf_detector_footprint_list_expand, SMD_RF_DETECTOR_SYMBOL],
  [CAT_SMD_RF_FILTER,  'output/sz_jlc_rf_filter.lib', 'output/sz_jlc_rf_filter.dcm', rf_filter_footprint_expand, rf_filter_footprint_list_expand, SMD_RF_FILTER_SYMBOL],
  [CAT_SMD_RF_MIXER,  'output/sz_jlc_rf_mixer.lib', 'output/sz_jlc_rf_mixer.dcm', rf_mixer_footprint_expand, rf_mixer_footprint_list_expand, SMD_RF_MIXER_SYMBOL],
  [CAT_SMD_RF_SWITCH,  'output/sz_jlc_rf_switch.lib', 'output/sz_jlc_rf_switch.dcm', rf_switch_footprint_expand, rf_switch_footprint_list_expand, SMD_RF_SWITCH_SYMBOL],
  [CAT_SMD_RS232_CHIP,  'output/sz_jlc_rs232_chip.lib', 'output/sz_jlc_rs232_chip.dcm', rs232_chip_footprint_expand, rs232_chip_footprint_list_expand, SMD_RS232_CHIP_SYMBOL],
  [CAT_SMD_RS485_RS422_CHIP,  'output/sz_jlc_rs485_rs422_chip.lib', 'output/sz_jlc_rs485_rs422_chip.dcm', rs485_rs422_chip_footprint_expand, rs485_rs422_chip_footprint_list_expand, SMD_RS485_RS422_CHIP_SYMBOL],
  [CAT_SMD_SCHOTTKY_DIODE,  'output/sz_jlc_schottky_diode.lib', 'output/sz_jlc_schottky_diode.dcm', schottky_diode_footprint_expand, schottky_diode_footprint_list_expand, SMD_SCHOTTKY_DIODE_SYMBOL],
  [CAT_SMD_SDRAM_MEMORY,  'output/sz_jlc_sdram_memory.lib', 'output/sz_jlc_sdram_memory.dcm', sdram_memory_footprint_expand, sdram_memory_footprint_list_expand, SMD_SDRAM_MEMORY_SYMBOL],
  [CAT_SMD_SECURITY_VERIFICATION_ENCRYPTION_CHIP,  'output/sz_jlc_security_verification_encryption_chip.lib', 'output/sz_jlc_security_verification_encryption_chip.dcm', security_verification_encryption_chip_footprint_expand, security_verification_encryption_chip_footprint_list_expand, SMD_SECURITY_VERIFICATION_ENCRYPTION_CHIP_SYMBOL],
  [CAT_SMD_SENSOR_INTERFACE_CHIP,  'output/sz_jlc_sensor_interface_chip.lib', 'output/sz_jlc_sensor_interface_chip.dcm', sensor_interface_chip_footprint_expand, sensor_interface_chip_footprint_list_expand, SMD_SENSOR_INTERFACE_CHIP_SYMBOL],
  [CAT_SMD_SERIAL_INTERFACE,  'output/sz_jlc_serial_interface.lib', 'output/sz_jlc_serial_interface.dcm', serial_interface_footprint_expand, serial_interface_footprint_list_expand, SMD_SERIAL_INTERFACE_SYMBOL],
  [CAT_SMD_SHIFT_REGISTER,  'output/sz_jlc_shift_register.lib', 'output/sz_jlc_shift_register.dcm', shift_register_footprint_expand, shift_register_footprint_list_expand, SMD_SHIFT_REGISTER_SYMBOL],
  [CAT_SMD_SIGNAL_BUFFERS_REPEATERS_DISTRIBUTORS,  'output/sz_jlc_signal_buffers_repeaters_distributors.lib', 'output/sz_jlc_signal_buffers_repeaters_distributors.dcm', signal_buffers_repeaters_distributors_footprint_expand, signal_buffers_repeaters_distributors_footprint_list_expand, SMD_SIGNAL_BUFFERS_REPEATERS_DISTRIBUTORS_SYMBOL],
  [CAT_SMD_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS,  'output/sz_jlc_signal_switches_multiplexers_decoders.lib', 'output/sz_jlc_signal_switches_multiplexers_decoders.dcm', signal_switches_multiplexers_decoders_footprint_expand, signal_switches_multiplexers_decoders_footprint_list_expand, SMD_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS_SYMBOL],
  [CAT_SMD_SOLID_ELECTROLYTIC_CAPACITOR,  'output/sz_jlc_solid_electrolytic_capacitor.lib', 'output/sz_jlc_solid_electrolytic_capacitor.dcm', solid_electrolytic_capacitor_footprint_expand, solid_electrolytic_capacitor_footprint_list_expand, SMD_SOLID_ELECTROLYTIC_CAPACITOR_SYMBOL],
  [CAT_SMD_SOUND_SURFACE_RESONATOR_SAW,  'output/sz_jlc_sound_surface_resonator_saw.lib', 'output/sz_jlc_sound_surface_resonator_saw.dcm', sound_surface_resonator_saw_footprint_expand, sound_surface_resonator_saw_footprint_list_expand, SMD_SOUND_SURFACE_RESONATOR_SAW_SYMBOL],
  [CAT_SMD_SPECIAL_FUNCTION_AMPLIFIER,  'output/sz_jlc_special_function_amplifier.lib', 'output/sz_jlc_special_function_amplifier.dcm', special_function_amplifier_footprint_expand, special_function_amplifier_footprint_list_expand, SMD_SPECIAL_FUNCTION_AMPLIFIER_SYMBOL],
  [CAT_SMD_SPECIAL_FUNCTION_DRIVEN,  'output/sz_jlc_special_function_driven.lib', 'output/sz_jlc_special_function_driven.dcm', special_function_driven_footprint_expand, special_function_driven_footprint_list_expand, SMD_SPECIAL_FUNCTION_DRIVEN_SYMBOL],
  [CAT_SMD_SRAM_MEMORY,  'output/sz_jlc_sram_memory.lib', 'output/sz_jlc_sram_memory.dcm', sram_memory_footprint_expand, sram_memory_footprint_list_expand, SMD_SRAM_MEMORY_SYMBOL],
  [CAT_SMD_SWITCHING_DIODE,  'output/sz_jlc_switching_diode.lib', 'output/sz_jlc_switching_diode.dcm', switching_diode_footprint_expand, switching_diode_footprint_list_expand, SMD_SWITCHING_DIODE_SYMBOL],
  [CAT_SMD_SWITCHING_POWER_CHIP,  'output/sz_jlc_switching_power_chip.lib', 'output/sz_jlc_switching_power_chip.dcm', switching_power_chip_footprint_expand, switching_power_chip_footprint_list_expand, SMD_SWITCHING_POWER_CHIP_SYMBOL],
  [CAT_SMD_TACT_SWITCH,  'output/sz_jlc_tact_switch.lib', 'output/sz_jlc_tact_switch.dcm', tact_switch_footprint_expand, tact_switch_footprint_list_expand, SMD_TACT_SWITCH_SYMBOL],
  [CAT_SMD_TANTALUM_CAPACITOR,  'output/sz_jlc_tantalum_capacitor.lib', 'output/sz_jlc_tantalum_capacitor.dcm', tantalum_capacitor_footprint_expand, tantalum_capacitor_footprint_list_expand, SMD_TANTALUM_CAPACITOR_SYMBOL],
  [CAT_SMD_TEMPERATURE_AND_HUMIDITY_SENSOR,  'output/sz_jlc_temperature_and_humidity_sensor.lib', 'output/sz_jlc_temperature_and_humidity_sensor.dcm', temperature_and_humidity_sensor_footprint_expand, temperature_and_humidity_sensor_footprint_list_expand, SMD_TEMPERATURE_AND_HUMIDITY_SENSOR_SYMBOL],
  [CAT_SMD_TEMPERATURE_SENSOR,  'output/sz_jlc_temperature_sensor.lib', 'output/sz_jlc_temperature_sensor.dcm', temperature_sensor_footprint_expand, temperature_sensor_footprint_list_expand, SMD_TEMPERATURE_SENSOR_SYMBOL],
  [CAT_SMD_THYRISTOR,  'output/sz_jlc_thyristor.lib', 'output/sz_jlc_thyristor.dcm', thyristor_footprint_expand, thyristor_footprint_list_expand, SMD_THYRISTOR_SYMBOL],
  [CAT_SMD_TIME_BASE_INTEGRATED_CHIP,  'output/sz_jlc_time_base_integrated_chip.lib', 'output/sz_jlc_time_base_integrated_chip.dcm', time_base_integrated_chip_footprint_expand, time_base_integrated_chip_footprint_list_expand, SMD_TIME_BASE_INTEGRATED_CHIP_SYMBOL],
  [CAT_SMD_TOUCH_CHIP,  'output/sz_jlc_touch_chip.lib', 'output/sz_jlc_touch_chip.dcm', touch_chip_footprint_expand, touch_chip_footprint_list_expand, SMD_TOUCH_CHIP_SYMBOL],
  [CAT_SMD_TOUCH_SCREEN_CONTROLLER,  'output/sz_jlc_touch_screen_controller.lib', 'output/sz_jlc_touch_screen_controller.dcm', touch_screen_controller_footprint_expand, touch_screen_controller_footprint_list_expand, SMD_TOUCH_SCREEN_CONTROLLER_SYMBOL],
  [CAT_SMD_TRIGGER_DIODE,  'output/sz_jlc_trigger_diode.lib', 'output/sz_jlc_trigger_diode.dcm', trigger_diode_footprint_expand, trigger_diode_footprint_list_expand, SMD_TRIGGER_DIODE_SYMBOL],
  [CAT_SMD_TRIGGER,  'output/sz_jlc_trigger.lib', 'output/sz_jlc_trigger.dcm', trigger_footprint_expand, trigger_footprint_list_expand, SMD_TRIGGER_SYMBOL],
  [CAT_SMD_TRIODE_DIGITAL_TRIODE,  'output/sz_jlc_triode_digital_triode.lib', 'output/sz_jlc_triode_digital_triode.dcm', triode_digital_triode_footprint_expand, triode_digital_triode_footprint_list_expand, SMD_TRIODE_DIGITAL_TRIODE_SYMBOL],
  [CAT_SMD_TRIODE,  'output/sz_jlc_triode.lib', 'output/sz_jlc_triode.dcm', triode_footprint_expand, triode_footprint_list_expand, SMD_TRIODE_SYMBOL],
  [CAT_SMD_TVS_DIODE,  'output/sz_jlc_tvs_diode.lib', 'output/sz_jlc_tvs_diode.dcm', tvs_diode_footprint_expand, tvs_diode_footprint_list_expand, SMD_TVS_DIODE_SYMBOL],
  [CAT_SMD_ULTRA_FAST_RECOVERY_DIODE,  'output/sz_jlc_ultra_fast_recovery_diode.lib', 'output/sz_jlc_ultra_fast_recovery_diode.dcm', ultra_fast_recovery_diode_footprint_expand, ultra_fast_recovery_diode_footprint_list_expand, SMD_ULTRA_FAST_RECOVERY_DIODE_SYMBOL],
  [CAT_SMD_USB_CHIP,  'output/sz_jlc_usb_chip.lib', 'output/sz_jlc_usb_chip.dcm', usb_chip_footprint_expand, usb_chip_footprint_list_expand, SMD_USB_CHIP_SYMBOL],
  [CAT_SMD_VARICAP_DIODE,  'output/sz_jlc_varicap_diode.lib', 'output/sz_jlc_varicap_diode.dcm', varicap_diode_footprint_expand, varicap_diode_footprint_list_expand, SMD_VARICAP_DIODE_SYMBOL],
  [CAT_SMD_VARISTOR,  'output/sz_jlc_varistor.lib', 'output/sz_jlc_varistor.dcm', varistor_footprint_expand, varistor_footprint_list_expand, SMD_VARISTOR_SYMBOL],
  [CAT_SMD_VIDEO_AND_AUDIO_INTERFACE_CHIP,  'output/sz_jlc_video_and_audio_interface_chip.lib', 'output/sz_jlc_video_and_audio_interface_chip.dcm', video_and_audio_interface_chip_footprint_expand, video_and_audio_interface_chip_footprint_list_expand, SMD_VIDEO_AND_AUDIO_INTERFACE_CHIP_SYMBOL],
  [CAT_SMD_VIDEO_FILTER_DRIVER,  'output/sz_jlc_video_filter_driver.lib', 'output/sz_jlc_video_filter_driver.dcm', video_filter_driver_footprint_expand, video_filter_driver_footprint_list_expand, SMD_VIDEO_FILTER_DRIVER_SYMBOL],
  [CAT_SMD_VOLTAGE_COMPARATOR,  'output/sz_jlc_voltage_comparator.lib', 'output/sz_jlc_voltage_comparator.dcm', voltage_comparator_footprint_expand, voltage_comparator_footprint_list_expand, SMD_VOLTAGE_COMPARATOR_SYMBOL],
  [CAT_SMD_VOLTAGE_REFERENCE_CHIP,  'output/sz_jlc_voltage_reference_chip.lib', 'output/sz_jlc_voltage_reference_chip.dcm', voltage_reference_chip_footprint_expand, voltage_reference_chip_footprint_list_expand, SMD_VOLTAGE_REFERENCE_CHIP_SYMBOL],
  [CAT_SMD_WIRELESS_TRANSCEIVER_CHIP,  'output/sz_jlc_wireless_transceiver_chip.lib', 'output/sz_jlc_wireless_transceiver_chip.dcm', wireless_transceiver_chip_footprint_expand, wireless_transceiver_chip_footprint_list_expand, SMD_WIRELESS_TRANSCEIVER_CHIP_SYMBOL],
]

def lookup_drawing_by_category(component_category):
  output = list(lookup_master_table_by_category(component_category))
  try:
    if (len(output) == 1):
      return output[0][5]
    else:
      raise 'lookup_drawing_by_category error'
  except Exception as e:
    pprint('lookup_drawing_by_category error')
    raise e
    pass


def lookup_master_table_by_category(component_category):
  return list(filter(lambda x: x[0]==component_category, master_table))