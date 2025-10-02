""""Mini redis storage engine """
import time
import threading
from typing import Any, Dict,  Optional
from collections import OrderedDict
class RedisStorage:
   def __init__(self):
    self._store: Dict[str, Any] = OrderedDict()
    self._expires: Dict[str, float] = {}
    self._lock = threading.Lock()
    self._stats={
      'total_commands':0,
      'get_commands':0,
      'set_commands':0,
      'hits':0,
      'misses':0
    }
   def set(self,key:str,value:Any,expire_seconds:Optional[int]=None)->str:
      with self._lock:
         self._store[key]=value
         if expire_seconds:
            self._expires[key]=time.time()+expire_seconds
         elif key in self._expires:
            del self._expires[key]
         self._stats['total_commands']+=1
         self._stats['set_commands']+=1
         return "ok"
   def get(self,key:str)->Optional[Any]:
      with self._lock:
         self._stats['total_commands']+=1
         self._stats['get_commands']+=1
         if key in self._expires:
            if time.time()>self._expires[key]:
               del self._store[key]
               del self._expires[key]
               self._stats['misses']+=1
               return None
         if key in self._store:
            self._stats['hits']+=1
            return self._store[key]
         self._stats["misses"]+=1
         return None
   def delete(self,key:str)->int:
      with self._lock:
         if key in self._store:
            del self._store[key]
            if key in self._expires:
               del self._expires[key]
            return 1
         return 0
   def exists(self,key:str)->bool:
      with self._lock:
         return key in self._store 
   def expire(self,key:str,seconds:int)->int:
      with self._lock:
         if key in self._store:
            self._expires[key]=time.time()+seconds
            return 1
         return 0
   def ttl(self,key:str)->int:
      with self._lock:
         if key not in self._estoxpir:
            return -2
         if key not in self._expires:
            return -1
         ttl=int(self._expires[key]-time.time())
         return(max(ttl,0))
   def flushall(self):
      with self._lock:
         self._store.clear()
         self._expires.clear()
   def dbsize(self)->int:
      with self._lock:
         return(len(self._store))
   def info(self)->dict:
      return {
         'keys':len(self._store),
         'expires':len(self._expires),
         **self._stats
      }
if __name__ == "__main__":
    # Testez votre implémentation
    redis = RedisStorage()
    
    # Test SET/GET
    print(redis.set("name", "Alice"))  # OK
    print(redis.get("name"))  # Alice
    
    # Test expiration
    redis.set("temp", "data", expire_seconds=2)
    print(redis.get("temp"))  # data
    time.sleep(3)
    print(redis.get("temp"))  # None
    
    # Test stats
    print(redis.info())