from rest_framework.throttling import SimpleRateThrottle
class FriendRequestThrottle(SimpleRateThrottle):
    scope = 'friend_request'
    rate = '3/minute'
    def get_cache_key(self, request, view):
        # Use the user's ID as part of the cache key to distinguish requests from different users
        user_id = request.user.id if request.user else None
        return f'{self.scope}-{user_id}'

    def allow_request(self, request, view):
        # Get the cache key for the current request
        cache_key = self.get_cache_key(request, view)
        # Get the number of requests made by the user within the throttle time window
        num_requests = self.cache.get(cache_key, 0)
        # Check if the user has exceeded the allowed number of requests
        if num_requests >= 3:
            return False
        # Increment the number of requests made by the user
        self.cache.set(cache_key, num_requests + 1, self.duration)
        return True