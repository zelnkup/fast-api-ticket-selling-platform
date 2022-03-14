import importlib
from typing import Any

from src.core.settings import settings


def resolve_dotted_path(path: str) -> Any:
    """
    Retrieves attribute (var, function, class, etc.) from module by dotted path
    .. code-block:: python
        from datetime.datetime import utcnow as default_utcnow
        utcnow = resolve_dotted_path('datetime.datetime.utcnow')
        assert utcnow == default_utcnow
    :param path: dotted path to the attribute in module
    :return: desired attribute or None
    """
    splitted = path.split(".")
    if len(splitted) <= 1:
        return importlib.import_module(path)
    module, attr = ".".join(splitted[:-1]), splitted[-1]
    module = importlib.import_module(module)
    return getattr(module, attr)


def get_user_model():
    """
    Gets user model class based on project settings.
    :return: User (default or custom) model class
    """
    return resolve_dotted_path(settings.USER_AUTH_MODEL)
