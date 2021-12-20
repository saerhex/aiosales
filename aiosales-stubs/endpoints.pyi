from typing import Dict

from fastapi.routing import APIRouter

router: APIRouter


def metrics() -> Dict[str, str]: ...
