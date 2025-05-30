# core/session.py

import time
import uuid

class Session:
    def __init__(self, profile_id="anon", start_ts=None):
        self.session_id = str(uuid.uuid4())
        self.profile_id = profile_id
        self.start_ts = start_ts or time.time()
        self.active = True

    def mark_expired(self):
        self.active = False

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "profile_id": self.profile_id,
            "start_ts": self.start_ts,
            "active": self.active
        }

if __name__ == "__main__":
    s = Session("test-profile")
    print(s.to_dict())
