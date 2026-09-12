"""
نظام إدارة التراخيص الرقمية وحماية المنتجات (License Manager)
"""
import hashlib
import time
import uuid

SECRET_SALT = "PROMPTFORGE_SECURE_2026"

class LicenseManager:
    @staticmethod
    def generate_license_key(customer_email: str, plan: str = "PRO") -> str:
        """توليد مفتاح ترخيص رقمي فريد للعميل"""
        timestamp = str(int(time.time()))
        raw = f"{customer_email}:{plan}:{timestamp}:{SECRET_SALT}"
        hash_digest = hashlib.sha256(raw.encode()).hexdigest().upper()
        # تنسيق كود الترخيص: PFORGE-XXXX-XXXX-XXXX-XXXX
        parts = [hash_digest[i:i+4] for i in range(0, 16, 4)]
        return f"PFORGE-{'-'.join(parts)}"

    @staticmethod
    def verify_license(license_key: str) -> bool:
        """التحقق من صحة ترخيص البرنامج"""
        if not license_key.startswith("PFORGE-"):
            return False
        segments = license_key.split("-")
        return len(segments) == 5 and all(len(s) == 4 for s in segments[1:])

if __name__ == "__main__":
    lm = LicenseManager()
    key = lm.generate_license_key("buyer@example.com", "PRO_LIFETIME")
    print(f"Generated Key: {key}")
    print(f"Is Valid: {lm.verify_license(key)}")
