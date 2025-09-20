from fastapi import APIRouter
from fastapi.responses import Response


from prometheus_client import (generate_latest)


router = APIRouter(prefix='', include_in_schema=False)


@router.get('/metrics')
async def get_metrics():
    return Response(generate_latest())
