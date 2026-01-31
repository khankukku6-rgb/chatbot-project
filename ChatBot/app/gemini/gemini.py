import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    async def chat(self, system_prompt: str, user_message: str) -> str:
        full_prompt = f"""
{system_prompt}

User: {user_message}
""".strip()

        response = self.model.generate_content(full_prompt)
        return response.text
