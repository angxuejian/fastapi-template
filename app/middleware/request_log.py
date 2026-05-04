from fastapi import Request
import time


async def request_log(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    end = (time.time() - start) * 1000

    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(f"{GREEN}~~~~{RESET}      {request.method} {request.url} - {end:.3f}ms")

    return response