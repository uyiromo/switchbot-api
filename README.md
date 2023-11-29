# SwitchBot API
- https://github.com/OpenWonderLabs/SwitchBotAPI

# NOT TESTED, NOT DOCUMENTED

# Example
```
#!/usr/bin/env python3

from time import sleep
from switchbotapi import api_init, show_device_list, PlugMiniJP

token: str = "xxxxxxxxxxx"
secret: str = "yyyyyyyyyyy"

if __name__ == "__main__":
    api_init(token, secret)
    show_device_list()

    plug: PlugMiniJP = PlugMiniJP("zzzzzzzz")
    print(plug.dump(4))

    if plus.is_poweron():
        plug.power_off()
    else:
        plug.power_on()
    sleep(10)
    plug.power_toggle()

    print(plug.dump(4))

```
