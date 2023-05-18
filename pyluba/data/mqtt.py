from base64 import b64decode
from typing import Literal

from pydantic import BaseModel

from pyluba.data import luba_pb2


class Base64EncodedProtobuf:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        if not isinstance(v, str):
            raise TypeError("string required")
        binary = b64decode(v, validate=True)
        data = luba_pb2.Root()
        data.ParseFromString(binary)
        return data


class Value(BaseModel):
    content: Base64EncodedProtobuf


class Params(BaseModel):
    identifier: Literal["device_protobuf_msg_event"]
    groupIdList: list[str]
    groupId: str
    categoryKey: Literal["LawnMower"]
    batchId: str
    gmtCreate: int
    productKey: str
    type: Literal["info"]
    deviceName: str
    iotId: str
    checkLevel: int
    namespace: str
    tenantId: str
    name: str
    thingType: Literal["DEVICE"]
    time: int
    tenantInstanceId: str
    value: Value


class ThingEventMessage(BaseModel):
    method: Literal["thing.events"]
    id: str
    params: Params
    version: Literal["1.0"]
