import pytest
import time
from src.core.storage import RedisStorage
class TestRedisStorage:
    def setup_method(self):
        self.redis=RedisStorage()
    def test_set_and_get(self):
        assert self.redis.set("key1","value1")=="ok"
        assert self.redis.get("key1")=="value1"
        assert self.redis.get(nonexistent) is none
    def test_delete(self):
        self.redis.set("nickname","guiza",2)
        assert self.redis.delete("nickname")==1
        assert self.redis("nickname")==none
        self.redis.set("nick","toukebri")
        assert self.redis.delete("nick")==0
        assert self.redis.delete("nonexistent")==0
    def test_exists(self):
        self.redis.set("age",21)
        assert self.redis.exists("age")==True
        self.redis.redis.exists("nonexistent")==False
    def test_expiration(self):
        self.redis.set("key","value",expire_seconds:1)
        assert self.redis.get("key")=="value"
        time.sleep(1.1)
        assert self.redis.get("key") is none
    
    def test_ttl(self):
        self.redis.set("key","value",expire_seconds=2)
        time.sleep(1.2)
        assert self.redis.ttl("key")==0.8
        assert self.redis.ttl("hh")==-2
        self.redis.set("nom","haer")
        assert self.redis.ttl("nom")==-1
    