# coding: utf-8

"""
    Multilogin X Profile Access Management API

    Multilogin X Profile Access Management API allows you to control everything related to permissions, workspaces, team members.

    The version of the OpenAPI document: 1.0.0
    Contact: support@multilogin.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pam_api_client.models.browser_type import BrowserType
from pam_api_client.models.rate_limit import RateLimit
from typing import Optional, Set
from typing_extensions import Self

class Restriction(BaseModel):
    """
    Restriction
    """ # noqa: E501
    plan_name: StrictStr
    cloud_profiles_count: Annotated[int, Field(strict=True, ge=0)]
    local_profiles_count: Annotated[int, Field(strict=True, ge=0)]
    folders_count: Annotated[int, Field(le=500, strict=True, ge=1)]
    team_members_count: Annotated[int, Field(strict=True, ge=0)]
    canceled: Optional[StrictBool] = None
    expires_at: Optional[StrictInt] = None
    automation_available: Optional[StrictBool] = None
    allowed_browser_types: Annotated[List[BrowserType], Field(min_length=1, max_length=3)]
    ratelimit: Optional[List[RateLimit]] = None
    __properties: ClassVar[List[str]] = ["plan_name", "cloud_profiles_count", "local_profiles_count", "folders_count", "team_members_count", "canceled", "expires_at", "automation_available", "allowed_browser_types", "ratelimit"]

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
        """Create an instance of Restriction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ratelimit (list)
        _items = []
        if self.ratelimit:
            for _item in self.ratelimit:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ratelimit'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Restriction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan_name": obj.get("plan_name"),
            "cloud_profiles_count": obj.get("cloud_profiles_count"),
            "local_profiles_count": obj.get("local_profiles_count"),
            "folders_count": obj.get("folders_count"),
            "team_members_count": obj.get("team_members_count"),
            "canceled": obj.get("canceled"),
            "expires_at": obj.get("expires_at"),
            "automation_available": obj.get("automation_available"),
            "allowed_browser_types": obj.get("allowed_browser_types"),
            "ratelimit": [RateLimit.from_dict(_item) for _item in obj["ratelimit"]] if obj.get("ratelimit") is not None else None
        })
        return _obj


