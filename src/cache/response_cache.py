import hashlib


class ResponseCache:

    def __init__(self):

        self.cache = {}

    def _key(
        self,
        question: str,
        context: str
    ):

        raw = (
            question +
            context
        )

        return hashlib.md5(
            raw.encode()
        ).hexdigest()

    def get(
        self,
        question: str,
        context: str
    ):

        key = self._key(
            question,
            context
        )

        return self.cache.get(
            key
        )

    def set(
        self,
        question: str,
        context: str,
        answer: str
    ):

        key = self._key(
            question,
            context
        )

        self.cache[key] = answer