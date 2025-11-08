
import time

class XClient:
    def __init__(self, bearer_token: str | None = None):
        self.token = bearer_token

    def pull_recent(self, topics_or_handles, limit=50):
        now = int(time.time())
        return [{"topic": str(t), "likes": 10, "retweets": 2, "ts": now} for t in topics_or_handles]
