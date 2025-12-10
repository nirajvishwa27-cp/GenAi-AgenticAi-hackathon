from llm_setup import call_llm

class JuniorDeveloper:
    def run(self, user_request, style_guide):
        prompt = f"""
        ROLE:
        You are a Python Junior Developer. Your goal is to write production-ready code that passes a strict security review.

        INPUTS:
        1. User Feature Request: "{user_request}"
        2. Team Style Guide (Mandatory Rules):
        {style_guide}

        INSTRUCTIONS:
        - Write a complete, functional Python script for the request.
        - You MUST follow every rule in the Style Guide. If you ignore a rule, your code will be rejected.
        - If the style guide warns against specific patterns (like hardcoded secrets), use alternatives (like os.getenv).
        - Include comments explaining complex logic.
        
        OUTPUT FORMAT:
        Return ONLY the Python code block. Do not add conversational text like "Here is the code".
        Just the code.
        """
        return call_llm(prompt)