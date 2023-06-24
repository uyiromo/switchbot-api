import json
from typing import Any

from .api import get_status, api_post
from .common import JSON


class SwitchBotDevice:
    def dump(self, indent: int) -> str:
        return json.dumps(self._js, sort_keys=True, ensure_ascii=False, indent=indent)

    def __str__(self) -> str:
        return self.dump(None)

    def __init__(self, device_id: str):
        self._js: JSON = dict()
        self._uninit: bool = True

    def _get(self, key: str) -> Any:
        self.renew()
        return self._js[key]

    @property
    def device_id(self) -> str:
        return str(self._get("deviceId"))

    @property
    def device_type(self) -> str:
        return str(self._get("deviceType"))

    @property
    def hub_device_id(self) -> str:
        return str(self._get("hubDeviceId"))

    def cmd(self, commands: JSON) -> None:
        api_post(
            f"/v1.1/devices/{self.device_id}/commands",
            commands,
        )
        self._uninit = True

    def renew(self) -> None:
        if self._uninit:
            self._js = get_status(self.device_id)
        self._uninit = False
