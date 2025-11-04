from enum import StrEnum

from fastapi import APIRouter

from backend.api.custom import RouteErrorHandler
from backend.api.endpoints.healthcheck import router as router_healthcheck

router = APIRouter(route_class=RouteErrorHandler)


class RouterPrefix(StrEnum):
    HEALTH_CHECK = "/healthcheck"


router.include_router(router=router_healthcheck, prefix=RouterPrefix.HEALTH_CHECK.value)
