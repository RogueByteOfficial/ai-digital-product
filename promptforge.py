"""
PromptForge Pro - AI Prompt Engineering & Automation Toolkit
A production-ready Python utility for prompt engineering, token cost estimation, and schema validation.
"""
import json
import hashlib
import time

class PromptForge:
    def __init__(self, app_name="PromptForge Pro", version="1.0.0"):
        self.app_name = app_name
        self.version = version

    def optimize_prompt(self, raw_prompt: str, target_model: str = "qwen2.5-coder") -> dict:
        """تحسين وتنسيق الـ Prompt تلقائياً بأفضل الممارسات"""
        cleaned = raw_prompt.strip()
        enhanced = (
            f"### Role & Objective:\n"
            f"You are an expert AI system specialized in high-performance execution for {target_model}.\n\n"
            f"### Primary Instruction:\n"
            f"{cleaned}\n\n"
            f"### Output Constraints:\n"
            f"- Be precise, concise, and production-ready.\n"
            f"- Return strictly structured output without conversational filler."
        )
        token_estimate = len(enhanced.split()) * 1.3
        return {
            "status": "success",
            "original_prompt": raw_prompt,
            "optimized_prompt": enhanced,
            "target_model": target_model,
            "estimated_tokens": int(token_estimate),
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def estimate_cost(self, token_count: int, input_price_per_1k: float = 0.0002) -> float:
        """حساب التكلفة التقديرية للرموز"""
        return round((token_count / 1000.0) * input_price_per_1k, 6)

    def generate_few_shot_template(self, task_type: str, examples: list) -> str:
        """توليد قالب Few-Shot مبرمج"""
        template = f"# Few-Shot Prompt Template for: {task_type}\n\n"
        for i, ex in enumerate(examples, 1):
            template += f"Example {i}:\nInput: {ex.get('input', '')}\nOutput: {ex.get('output', '')}\n\n"
        template += "Now solve the user input below:\nInput: {{USER_INPUT}}\nOutput:"
        return template

if __name__ == "__main__":
    forge = PromptForge()
    sample = forge.optimize_prompt("Create a Python script to sort files by extension")
    print(json.dumps(sample, indent=2, ensure_ascii=False))
