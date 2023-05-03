from .device import SwitchBotDevice


class PlugMiniJP(SwitchBotDevice):
    """Plug Mini (JP): W2001400, W2001401"""

    def __init__(self, device_id: str):
        super().__init__(device_id)

    @property
    def voltage(self) -> float:
        """float: the voltage of the device, measured in Volt"""
        return float(self._get("voltage"))

    @property
    def version(self) -> str:
        """str: the current BLE and Wi-Fi firmware version, e.g. V3.1-6.3"""
        return str(self._get("version"))

    @property
    def weight(self) -> float:
        """float: the power consumed in a day, measured in Watts"""
        return float(self._get("weight"))

    @property
    def electricity_of_day(self) -> int:
        """int: the duration that the device has been used during a day, measured in minutes"""
        return int(self._get("electricityOfDay"))

    @property
    def electric_current(self) -> float:
        """float: the current of the device at the moment, measured in Amp"""
        return float(self._get("electricCurrent"))

    def power_on(self) -> None:
        self.cmd(
            {"commandType": "command", "command": "turnOn", "parameter": "default"}
        )

    def power_off(self) -> None:
        self.cmd(
            {"commandType": "command", "command": "turnOff", "parameter": "default"}
        )

    def power_toggle(self) -> None:
        self.cmd(
            {"commandType": "command", "command": "toggle", "parameter": "default"}
        )

    def is_poweron(self) -> bool:
        self.renew()
        return bool(self._get("power"))
