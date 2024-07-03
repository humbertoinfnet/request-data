import uvicorn
from src.external_interfaces.fastapi import app

if __name__ == "__main__":
    
    uvicorn.run(
        app,
        host="0.0.0.0",  # nosec
        port=3000,
        reload=False,
        log_config=uvicorn.config.LOGGING_CONFIG,
    )
