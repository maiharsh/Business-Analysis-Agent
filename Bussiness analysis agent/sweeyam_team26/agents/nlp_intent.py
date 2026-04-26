import re

def classify_intent(text):
    text = text.lower()

    if re.search(r"\bwhat if\b|\bif i don't\b|\bignore\b|\bdo nothing\b", text):
        return "WHAT_IF"

    if re.search(r"\bdomain\b|\bcategory\b|\bsimilar products\b|\bother products\b", text):
        return "DOMAIN_ANALYSIS"

    if re.search(r"\brisk\b|\bissue\b|\bproblem\b|\bstatus\b", text):
        return "RISK_STATUS"

    if re.search(r"\bperformance\b|\bmetrics\b|\bstats\b", text):
        return "SELLER_METRICS"

    if re.search(r"\bdecision\b|\brecommend\b|\bsuggest\b|\baction\b", text):
        return "DECISION"

    if re.search(r"\bsummary\b|\boverview\b|\bexecutive\b", text):
        return "SUMMARY"

    return "UNKNOWN"
