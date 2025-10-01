""""Mini redis storage engine """
import time
import threading
from typing import Any, Dict,  Optional
from collections import OrderedDict
class RedisStorage:
 def __int__(self):
    self._store: Dict[str, Any] = OrderedDict()
    self._expires: Dict[str, float] = {}
    self._lock = threading.Lock()