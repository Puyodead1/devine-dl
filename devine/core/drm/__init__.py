from typing import Union

from devine.core.drm.clearkey import ClearKey
from devine.core.drm.playready import PlayReady
from devine.core.drm.widevine import Widevine

DRM_T = Union[ClearKey, Widevine, PlayReady]


__all__ = ("ClearKey", "Widevine", "PlayReady", "DRM_T")
