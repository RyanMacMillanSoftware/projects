'''
Test suite for interview.py
'''
import pytest
import time
import uuid

from rate_limiter.src.rate_limiter import TokenBucketRateLimiter

test_data = [
        (1, 1, True), 
        (100, 100, True), 
        # Too hard to test under 100-120rps because the surrounding code takes enough time to simulate sub 100 rps
        (100, 120, False), 
        (100, 500, False), 
]

@pytest.mark.parametrize("requests, rps, expected", test_data)
def test_is_allow(requests, rps, expected):
    '''
    Clients are not allowed to make requests if they exceed 100 tests
    '''
    
    rate_limiter = TokenBucketRateLimiter()
    client_id = uuid.uuid4()
    
    num_calls = 0
    while num_calls < requests:
        allowed = rate_limiter.is_allow(client_id)
        time.sleep(1/rps)
        num_calls += 1
    assert allowed == expected
    
    
def test_is_allow_concurrent_clients():
    '''
    A client should still be allowed if another client has exceeded it's rate limit
    '''
    rate_limiter = TokenBucketRateLimiter()
    client_id_1 = uuid.uuid4()
    client_id_2 = uuid.uuid4()
    
    num_calls = 0
    while num_calls < 101:
        rate_limiter.is_allow(client_id_1)
        num_calls += 1
        
    allowed = rate_limiter.is_allow(client_id_2)
    assert allowed == True


def test_is_allow_after_waiting():
    '''
    A client should be allowed if it has exceeded it's rate limit and if it waits one second
    '''
    rate_limiter = TokenBucketRateLimiter()
    client_id_1 = uuid.uuid4()
    
    num_calls = 0
    while num_calls < 3:
        allowed = rate_limiter.is_allow(client_id_1)
        num_calls += 1
    assert allowed == False
    
    time.sleep(0.01)
        
    allowed = rate_limiter.is_allow(client_id_1)
    assert allowed == True