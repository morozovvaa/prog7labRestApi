from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY = "secret-api-key-12345"
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Проверка API ключа.
    Если ключ неверный, возвращается ошибка 403.
    """
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверный API ключ"
        )
    return api_key