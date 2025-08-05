import os
import requests

class ViettelAPIClient:
    def __init__(self):
        self.api_url = "https://viettelai.vn/tts/speech_synthesis"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_audio_file(self, text, speaker_id, speaker_name_friendly, output_dir, filename_prefix="viettel_"):
        """
        Gửi yêu cầu tổng hợp giọng nói Viettel với text và speaker_id.
        Lưu file âm thanh về output_dir với tên file có tiền tố filename_prefix.
        Trả về đường dẫn file audio, hoặc None nếu thất bại.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        filename = f"{filename_prefix}{int(time.time()*1000)}.mp3"
        filepath = os.path.join(output_dir, filename)

        body = {
            "speed": 1,
            "voice": speaker_id,
            "text": text,
            "tts_return_option": 3,
            "without_filter": False
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=body)
            if response.status_code == 200:
                with open(filepath, "wb") as f:
                    f.write(response.content)
                return filepath
            else:
                print(f"[ViettelAPIClient] Lỗi API Viettel: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"[ViettelAPIClient] Exception khi gọi API Viettel: {e}")
            return None


import time
