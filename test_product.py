"""
اختبارات الجودة والتحقق التلقائي للمنتج الرقمي PromptForge Pro
"""
import sys
from promptforge import PromptForge
from license_manager import LicenseManager

def test_suite():
    print("=" * 60)
    print("🧪 بدء تشغيل اختبارات جودة المنتج البرمجي...")
    print("=" * 60)

    # 1. فحص محرك الأوامر
    forge = PromptForge()
    res = forge.optimize_prompt("Sort data by date")
    assert res["status"] == "success", "فشل تحسين الأمر"
    assert "### Role & Objective:" in res["optimized_prompt"], "فشل تضمين الهيكل"
    print("✅ 1. اختبار تحسين الأوامر (PromptForge.optimize_prompt): ناجح بنسبة 100%")

    # 2. فحص حاسبة التكلفة
    cost = forge.estimate_cost(5000)
    assert cost > 0, "فشل حساب التكلفة"
    print(f"✅ 2. اختبار حاسبة الرموز (PromptForge.estimate_cost): ناجح (التكلفة: ${cost})")

    # 3. فحص نظام التراخيص
    lm = LicenseManager()
    key = lm.generate_license_key("client@domain.com", "PRO")
    assert lm.verify_license(key) is True, "فشل التحقق من الترخيص"
    print(f"✅ 3. اختبار توليد التراخيص (LicenseManager.verify_license): ناجح (المفتاح: {key})")

    print("=" * 60)
    print("🎉 جميع الاختبارات اجتازت بنجاح والمنتج جاهز للنشر والبيع كلياً!")
    print("=" * 60)

if __name__ == "__main__":
    test_suite()
