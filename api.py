#!/usr/bin/env python3

import json
from time import time
from hashlib import sha256
import hmac
from base64 import b64encode
from uuid import uuid4
from typing import Dict

from requests import request

from .common import JSON


def dump_json(js: JSON) -> None:
    return json.dumps(js, ensure_ascii=False, indent=4, sort_keys=True)


def build_header(token: str, secret: str) -> Dict[str, str]:
    nonce: str = uuid4()
    stamp: int = int(round(time() * 1000))

    data: str = f"{token}{stamp}{nonce}"
    data_b: bytes = bytes(data, "utf-8")
    secret_b = bytes(secret, "utf-8")

    sign = b64encode(hmac.new(secret_b, msg=data_b, digestmod=sha256).digest())

    return {
        "Authorization": token,
        "Content-Type": "application/json",
        "charset": "utf8",
        "t": str(stamp),
        "sign": sign,
        "nonce": str(nonce),
    }


api_token: str = None
api_secret: str = None


def api_init(token: str, secret: str) -> None:
    global api_token, api_secret

    api_token = token
    api_secret = secret


def api_get(endpoint: str) -> JSON:
    global api_token, api_secret

    return request(
        "GET",
        f"https://api.switch-bot.com{endpoint}",
        headers=build_header(api_token, api_secret),
    ).json()["body"]


def api_post(endpoint: str, payload: JSON) -> None:
    global api_token, api_secret

    request(
        "POST",
        f"https://api.switch-bot.com{endpoint}",
        headers=build_header(api_token, api_secret),
        data=json.dumps(payload),
    )


def show_device_list() -> None:
    for js in api_get("/v1.1/devices")["deviceList"]:
        print(dump_json(js))


def get_status(device_id: str) -> JSON:
    return api_get(f"/v1.1/devices/{device_id}/status")
