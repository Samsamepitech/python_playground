from datetime import datetime
now = datetime.now()

class Email:
    def __init__(self,_body, _subject, _from, _to, _sent_at=None):

        self._body =_body
        self._subject =_subject
        self._from =_from
        self._to = _to
        self._created_at = now.strftime("%H:%M:%S")
        self._updated_at = now.strftime("%H:%M:%S")


#m = Email("body", "sujet", "moi", "toi")

#print(m._body, m._subject, m._from, m._to, m._created_at, m._updated_at)