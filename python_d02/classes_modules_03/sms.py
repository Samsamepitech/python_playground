from sendable import Sendable

class Sms(Sendable):
    def __init__(self,_body,_from, _to):
        self._body =_body
        self._from =_from
        self._to = _to
