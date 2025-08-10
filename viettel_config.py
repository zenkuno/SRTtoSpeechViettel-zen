# --- API Configuration ---
DEFAULT_SPEAKER_ID = "hn-quynhanhg"
DEFAULT_SPEAKER_NAME = "HN Quỳnh Anh"


DEFAULT_MAX_POLL_RETRIES = 12
DEFAULT_POLL_INTERVAL_SEC = 5


VIETTEL_SPEAKERS = {
    "hn-thanhtung": "HN Thanh Tùng",
    "hn-namkhanh": "HN Nam Khánh",
    "hn-tienquan": "HN Tiến Quân",
    "hcm-minhquan": "HCM Minh Quân",
    "hue-baoquoc": "Huế Bảo Quốc",
    "hn-quynhanh": "HN Quỳnh Anh",
    "hn-thanhphuong": "HN Thanh Phương",
    "hn-leyen": "HN Lê Yến",
    "hn-phuongtrang": "HN Phương Trang",
    "hn-thaochi": "HN Thảo Chi",
    "hn-thanhha": "HN Thanh Hà",
    "hcm-phuongly": "HCM Phương Ly",
    "hcm-thuydung": "HCM Thùy Dung",
    "hcm-diemmy": "HCM Diễm My",
    "hcm-thuyduyen": "HCM Thùy Duyên",
    "hue-maingoc": "Huế Mai Ngọc",

}

def get_default_speaker_id():
    return "hn-quynhanh"

def get_speaker_name(speaker_id):
    return VIETTEL_SPEAKERS.get(speaker_id, "Không rõ")

def get_default_speaker_name():
    return VIETTEL_SPEAKERS.get(DEFAULT_SPEAKER_ID, "Không rõ")
