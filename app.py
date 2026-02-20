from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

# 🟢 Liveness Probe (App is running)
@app.get("/health/live")
def liveness_check():
    return {"status": "alive"}

# 🟢 Readiness Probe (Dependencies check)
@app.get("/health/ready")
def readiness_check():
    try:
        # Example: check DB or external service
        # simulate success
        dependency_ok = True

        if dependency_ok:
            return {"status": "ready"}
        else:
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={"status": "not ready"},
            )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not ready", "error": str(e)},
        )
