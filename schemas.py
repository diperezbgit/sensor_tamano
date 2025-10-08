from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LecturaTamano(BaseModel):
    id: Optional[int] = None  # Se autogenera en la base de datos
    sensor_id: int
    valor: float
    timestamp: Optional[datetime] = None  # Se puede autogenerar en la base de datos