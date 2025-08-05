# Modules/List_API_Speech.py
import os

# Import Viettel module
try:
    from .viettel_api_client import ViettelAPIClient
    from . import viettel_config
except ImportError as e:
    ViettelAPIClient = None
    viettel_config = None
    print(f"LỖI (List_API_Speech): Không thể import Viettel module: {e}")

API_SPEECH_MODULES = {}

if ViettelAPIClient and viettel_config:
    viettel_client = ViettelAPIClient()
    API_SPEECH_MODULES["viettel"] = {
        "name": "Viettel API",
        "client": viettel_client,
        "speakers": viettel_config.VIETTEL_SPEAKERS if viettel_config else {},
        "get_default_speaker_id": viettel_config.get_default_speaker_id if viettel_config else lambda: ""
    }

