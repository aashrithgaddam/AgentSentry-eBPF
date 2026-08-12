import re
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="SentinelFabric Security Gateway")


class AgentRequest(BaseModel):
    prompt: str


BLACKLIST = [
    "ignore all safety",
    "ignore previous",
    "output the root",
    "cat /etc/",
]
PII_PATTERN = r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"


@app.get("/", response_class=HTMLResponse)
async def root_browser_view():
    return "<h1>SentinelFabric Security Gateway is ONLINE</h1>"


@app.post("/v1/execute")
async def secure_sentinel_proxy(request: AgentRequest):
    user_input = request.prompt.lower()

    if any(threat in user_input for threat in BLACKLIST):
        raise HTTPException(
            status_code=403,
            detail={
                "error": "Threat Detected",
                "reason": "Malicious Intent Blocked by Guardrail",
            },
        )

    sanitized_output = re.sub(PII_PATTERN, "[REDACTED_PII]", request.prompt)
    return {
        "status": "Verified",
        "agent_input": sanitized_output,
        "note": "Passed sentinel guardrails.",
    }


if __name__ == "__main__":
    import uvicorn

    # FIXED: String format used instead of raw object to ensure clean local loops on Windows
    uvicorn.run("sentinel_proxy:app", host="127.0.0.1", port=8000, reload=True)
