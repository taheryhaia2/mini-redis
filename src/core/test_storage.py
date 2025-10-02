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