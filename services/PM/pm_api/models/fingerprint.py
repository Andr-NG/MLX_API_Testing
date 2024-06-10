# coding: utf-8

"""
    Multilogin X Profile Management

    Multilogin X Profile Management API allows you to manage profiles.

    The version of the OpenAPI document: 1.0.0
    Contact: support@multilogin.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pm_api.models.cmd_params import CmdParams
from pm_api.models.geolocation import Geolocation
from pm_api.models.graphic import Graphic
from pm_api.models.localization import Localization
from pm_api.models.media_devices import MediaDevices
from pm_api.models.navigator import Navigator
from pm_api.models.screen import Screen
from pm_api.models.timezone import Timezone
from pm_api.models.webrtc import Webrtc
from typing import Optional, Set
from typing_extensions import Self

class Fingerprint(BaseModel):
    """
    Fingerprint
    """ # noqa: E501
    navigator: Optional[Navigator] = None
    localization: Optional[Localization] = None
    timezone: Optional[Timezone] = None
    graphic: Optional[Graphic] = None
    webrtc: Optional[Webrtc] = None
    fonts: Optional[List[Annotated[str, Field(min_length=3, strict=True, max_length=30)]]] = None
    media_devices: Optional[MediaDevices] = None
    screen: Optional[Screen] = None
    geolocation: Optional[Geolocation] = None
    ports: Optional[List[Annotated[int, Field(le=65535, strict=True, ge=0)]]] = None
    cmd_params: Optional[CmdParams] = None
    id: StrictStr
    meta_id: StrictStr
    __properties: ClassVar[List[str]] = ["navigator", "localization", "timezone", "graphic", "webrtc", "fonts", "media_devices", "screen", "geolocation", "ports", "cmd_params", "id", "meta_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Fingerprint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of navigator
        if self.navigator:
            _dict['navigator'] = self.navigator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of localization
        if self.localization:
            _dict['localization'] = self.localization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timezone
        if self.timezone:
            _dict['timezone'] = self.timezone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of graphic
        if self.graphic:
            _dict['graphic'] = self.graphic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webrtc
        if self.webrtc:
            _dict['webrtc'] = self.webrtc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_devices
        if self.media_devices:
            _dict['media_devices'] = self.media_devices.to_dict()
        # override the default output from pydantic by calling `to_dict()` of screen
        if self.screen:
            _dict['screen'] = self.screen.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geolocation
        if self.geolocation:
            _dict['geolocation'] = self.geolocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cmd_params
        if self.cmd_params:
            _dict['cmd_params'] = self.cmd_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Fingerprint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "navigator": Navigator.from_dict(obj["navigator"]) if obj.get("navigator") is not None else None,
            "localization": Localization.from_dict(obj["localization"]) if obj.get("localization") is not None else None,
            "timezone": Timezone.from_dict(obj["timezone"]) if obj.get("timezone") is not None else None,
            "graphic": Graphic.from_dict(obj["graphic"]) if obj.get("graphic") is not None else None,
            "webrtc": Webrtc.from_dict(obj["webrtc"]) if obj.get("webrtc") is not None else None,
            "fonts": obj.get("fonts"),
            "media_devices": MediaDevices.from_dict(obj["media_devices"]) if obj.get("media_devices") is not None else None,
            "screen": Screen.from_dict(obj["screen"]) if obj.get("screen") is not None else None,
            "geolocation": Geolocation.from_dict(obj["geolocation"]) if obj.get("geolocation") is not None else None,
            "ports": obj.get("ports"),
            "cmd_params": CmdParams.from_dict(obj["cmd_params"]) if obj.get("cmd_params") is not None else None,
            "id": obj.get("id"),
            "meta_id": obj.get("meta_id")
        })
        return _obj


