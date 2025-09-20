
from typing import List, Optional
from pydantic import BaseModel


class Data(BaseModel):
    url: str
    included_urls: Optional[List[str]] = None
    status_code: Optional[int] = None
