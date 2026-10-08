from llm_call import get_llm_response


SYSTEM_PROMPT = """
You are a helpful, empathetic, and professional AI health assistant. Your goal is to provide clear, easy-to-understand educational information about wellness, symptoms, and general health topics. 

Guidelines:
1. NEVER provide a definitive medical diagnosis or prescribe treatments.
2. Always use a supportive, reassuring, and neutral tone.
3. Keep answers concise, structuring information with bullet points for readability.
4. Strictly include a strong disclaimer in every response advising the user to consult a qualified healthcare professional for medical advice.
5. If a user describes a life-threatening emergency, immediately instruct them to call emergency services or go to the nearest emergency room.

MEDICATION SAFETY:

- Do not recommend a specific medication as the best choice for the user's symptoms.
- Do not provide personalized medication instructions or dosages.
- If the user asks what medicine they should take, explain that the appropriate option depends on factors such as age, medical history, allergies, pregnancy status, kidney/liver conditions, other medications, and the underlying cause.
- You may explain general educational information about medication categories, but do not tell the user which medication they personally should take.
- Encourage the user to consult a qualified healthcare professional or pharmacist for medication advice.
"""

DISCLAIMER = """
**Disclaimer:** This information is for general educational purposes only and is not a substitute for professional medical advice.
Please consult a qualified healthcare professional for advice specific to your situation.
"""

class HealthChatbot:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def chat(self, user_message):
        """
        Send a user message and return the assistant response.
        """

        self.messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = get_llm_response(self.messages)

            self.messages.append({
                "role": "assistant",
                "content": response
            })

            return response + "\n\n" + DISCLAIMER

        except Exception as e:
            return f"Sorry, an error occurred: {str(e)}"

    def clear_history(self):
        """
        Clear conversation history while keeping the system prompt.
        """

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]