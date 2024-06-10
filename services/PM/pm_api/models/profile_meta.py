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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pm_api.models.browser_type import BrowserType
from pm_api.models.profile_meta_update_params import ProfileMetaUpdateParams
from typing import Optional, Set
from typing_extensions import Self

class ProfileMeta(BaseModel):
    """
    ProfileMeta
    """ # noqa: E501
    folder_id: StrictStr
    workspace_id: StrictStr
    status: StrictStr
    created_at: datetime
    last_update_at: datetime
    removed_at: datetime
    removed_by: StrictStr
    browser_type: BrowserType
    os_type: StrictStr
    core_version: StrictInt
    name: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
    notes: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = None
    tags: Optional[List[Annotated[str, Field(min_length=1, strict=True, max_length=10)]]] = None
    parameters: ProfileMetaUpdateParams
    id: StrictStr
    __properties: ClassVar[List[str]] = ["folder_id", "workspace_id", "status", "created_at", "last_update_at", "removed_at", "removed_by", "browser_type", "os_type", "core_version", "name", "notes", "tags", "parameters", "id"]

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
        """Create an instance of ProfileMeta from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "folder_id": obj.get("folder_id"),
            "workspace_id": obj.get("workspace_id"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "last_update_at": obj.get("last_update_at"),
            "removed_at": obj.get("removed_at"),
            "removed_by": obj.get("removed_by"),
            "browser_type": obj.get("browser_type"),
            "os_type": obj.get("os_type"),
            "core_version": obj.get("core_version"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "tags": obj.get("tags"),
            "parameters": ProfileMetaUpdateParams.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "id": obj.get("id")
        })
        return _obj

