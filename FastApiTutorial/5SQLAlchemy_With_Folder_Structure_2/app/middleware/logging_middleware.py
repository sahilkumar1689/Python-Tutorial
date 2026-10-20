import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log incoming request
        logger.info(
            f"➡️ {request.method} {request.url.path} | IP: {request.client.host}"
        )

        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(f"🔥 Error processing request {request.url.path}: {str(e)}", exc_info=True)
            raise

        # Log response details
        process_time = (time.time() - start_time) * 1000
        logger.info(
            f"⬅️ {request.method} {request.url.path} | Status: {response.status_code} | "
            f"Time: {process_time:.2f}ms"
        )

        return response
