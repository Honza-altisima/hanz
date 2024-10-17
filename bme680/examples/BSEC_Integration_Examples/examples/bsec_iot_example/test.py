import bme680

sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

if sensor.get_sensor_data():
    print(f"Teplota: {sensor.data.temperature} °C")
    print(f"Vlhkost: {sensor.data.humidity} %")
    print(f"Tlak: {sensor.data.pressure} hPa")
    print(f"Plynový odpor: {sensor.data.gas_resistance} Ohms")

    if sensor.data.heat_stable:
        print(f"Kvalita vzduchu (IAQ): {sensor.data.iaq_score}")
    else:
        print("Kvalita vzduchu (IAQ) zatím není dostupná, senzor se stabilizuje...")

