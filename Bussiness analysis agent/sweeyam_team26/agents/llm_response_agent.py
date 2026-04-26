"""
LLM Response Agent
------------------
This agent is responsible ONLY for converting
structured agent outputs into natural language.

If the LLM is unavailable, it safely falls back
to deterministic text.
"""

import os

try:
    from openai import OpenAI
    _LLM_AVAILABLE = True
except ImportError:
    _LLM_AVAILABLE = False


def llm_response_agent(structured_response: dict) -> str:
    """
    Converts structured agent output into a human-friendly explanation.
    """

    # ---------- FALLBACK (NO LLM) ----------
    if not _LLM_AVAILABLE or not os.getenv("OPENAI_API_KEY"):
        return _fallback_response(structured_response)

    # ---------- LLM PATH ----------
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = (
        "You are a senior business surveillance analyst. "
        "Your task is to explain conclusions clearly and professionally. "
        "DO NOT add new facts. DO NOT change conclusions. "
        "ONLY explain what is provided."
    )

    user_prompt = _build_prompt(structured_response)

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )

        return completion.choices[0].message.content.strip()

    except Exception:
        return _fallback_response(structured_response)


# ============================================================
# INTERNAL HELPERS
# ============================================================

def _build_prompt(data: dict) -> str:
    """
    Builds a clean prompt from structured agent data.
    """

    return f"""
Explain the following surveillance findings in clear, professional language:

Domain: {data.get("domain")}
Scope: {data.get("scope")}
Affected Entity: {data.get("entity")}
Issue Type: {data.get("issue")}
Severity: {data.get("severity")}
Recommendation: {data.get("recommendation")}
"""


def _fallback_response(data: dict) -> str:
    """
    Deterministic explanation when LLM is unavailable.
    """

    scope_text = {
        "localized": "The issue is limited to a specific entity.",
        "domain-wide": "Multiple entities are affected across the domain.",
        "stable": "No significant risk patterns were detected."
    }.get(data.get("scope"), "Risk scope could not be determined.")

    return (
        f"📌 **Surveillance Explanation**\n\n"
        f"- Domain: {data.get('domain')}\n"
        f"- Scope: {data.get('scope')}\n"
        f"- Affected Entity: {data.get('entity')}\n"
        f"- Issue: {data.get('issue')}\n"
        f"- Severity: {data.get('severity')}\n\n"
        f"{scope_text}\n\n"
        f"**Recommended Action:** {data.get('recommendation')}"
    )
