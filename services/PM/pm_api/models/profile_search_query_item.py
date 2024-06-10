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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pm_api.models.browser_type import BrowserType
from typing import Optional, Set
from typing_extensions import Self

class ProfileSearchQueryItem(BaseModel):
    """
    ProfileSearchQueryItem
    """ # noqa: E501
    name: StrictStr = Field(description="Field used in text search")
    id: StrictStr
    is_local: StrictBool
    core_version: StrictInt
    os_type: StrictStr
    browser_type: BrowserType
    created_at: datetime
    updated_at: datetime
    removed_at: Optional[datetime] = None
    removed_by: Optional[StrictStr] = None
    folder_id: StrictStr
    notes: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    __properties: ClassVar[List[str]] = ["name", "id", "is_local", "core_version", "os_type", "browser_type", "created_at", "updated_at", "removed_at", "removed_by", "folder_id", "notes"]

    @field_validator('os_type')
    def os_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['linux', 'macos', 'windows', 'android']):
            raise ValueError("must be one of enum values ('linux', 'macos', 'windows', 'android')")
        return value

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
        """Create an instance of ProfileSearchQueryItem from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileSearchQueryItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "is_local": obj.get("is_local"),
            "core_version": obj.get("core_version"),
            "os_type": obj.get("os_type"),
            "browser_type": obj.get("browser_type"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "removed_at": obj.get("removed_at"),
            "removed_by": obj.get("removed_by"),
            "folder_id": obj.get("folder_id"),
            "notes": obj.get("notes")
        })
        return _obj

