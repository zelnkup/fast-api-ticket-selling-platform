from src.core.utils import get_user_model


User = get_user_model()


async def get_user_scopes(user: User) -> list[str]:
    scopes = []
    if user.is_superuser:
        scopes.append("admin")

    return scopes
