from llm_setup import call_llm

class TechLead:
    def run(self, code, audit_report):
        prompt = f"""
        ROLE:
        You are a decisive Tech Lead. You are responsible for the quality and security of the codebase.
        You must review the code and the security audit report to make a final decision.

        INPUTS:
        1. Audit Report (from Security Auditor):
        {audit_report}

        2. Proposed Code (from Junior Dev):
        {code}

        INSTRUCTIONS:
        - If the Audit Report contains ANY "CRITICAL" issues, you MUST reject the code (VERDICT: NO).
        - If the Audit Report has only minor style suggestions, you can approve it (VERDICT: YES) but still suggest improvements.
        - If you reject, define a NEW RULE for the Style Guide to prevent this mistake in the future.

        OUTPUT FORMAT (Strict):
        Respond in this EXACT format:
        VERDICT: [YES or NO]
        REASON: [Short explanation of why you approved or rejected]
        Add to style guide: [One short, clear rule to prevent this error, or "None" if valid]
        """
        return call_llm(prompt)