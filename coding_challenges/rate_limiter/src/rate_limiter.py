'''
Whenever you expose a web service / api endpoint, you need to implement a rate limiter to prevent abuse of the service (DOS attacks).


Implement a RateLimiter Class with an isAllow method. Every request comes in with a unique clientID, deny a request if that client has made more than 100 requests in the past second.

Source: https://leetcode.com/discuss/interview-question/system-design/124558/Uber-or-Rate-Limiter
'''

import time
        

class MyFirstRateLimiter():
    
    def __init__(self, ):
        self.rps = 100
        self.client_id_map = dict()
    
    def is_allow(self, client_id: str) -> bool:
        now = time.time()
        time_first_event, request_count = self.client_id_map.get(client_id, (now, 0))
        
        # A new second has begun for the client and their request counter can be reset
        if time_first_event < now - 1:
            time_first_event = now
            request_count = 1
            return True
        else:
            # Increment the request counter
            request_count += 1
            # Check if we exceeded the limit
            if request_count > self.rps:
                return False
            self.client_id_map[client_id] = (time_first_event, request_count)
        return True
        

class TokenBucketRateLimiter():
    
    def __init__(self, ):
        self.rps = 100
        self.client_id_map = dict()
    
    def is_allow(self, client_id: str) -> bool:
        now = time.time()
        last_event_time, tokens = self.client_id_map.get(client_id, (now, 1))
        
        # Add tokens to bucket for elapsed time
        seconds_elapsed = now - last_event_time
        tokens += int(seconds_elapsed * self.rps)
        tokens = min(tokens, self.rps) # never allow them to exceed the number of tokens they can use in one second
        
        # Check token in bucket
        if not tokens:
            return False
        
        # If there is a token in bucket, remove one token and allow
        tokens -= 1
        self.client_id_map[client_id] = (now, tokens)
        return True
        
        
