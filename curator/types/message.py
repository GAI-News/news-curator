from dataclasses import dataclass
from typing import Optional


@dataclass
class Message:
    sender: Optional[str] = None
    text: Optional[str] = None
