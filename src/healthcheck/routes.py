from fastapi import APIRouter, Response, status
from datetime import datetime


from .healthcheck import HealthCheck


router = APIRouter(prefix='', include_in_schema=False)


@router.get('/healthy')
async def healthcheck(response: Response):
    healthy = HealthCheck.get_status()
    if healthy:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return {
        'status': healthy,
        'date': datetime.now()
    }
