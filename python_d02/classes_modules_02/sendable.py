from datetime import datetime
now = datetime.now()


class Sendable:
    def __init__(self,_body, _subject, _from, _to, _sent_at=None):

        self._body =_body
        self._subject =_subject
        self._from =_from
        self._to = _to
        self._created_at = now.strftime("%H:%M:%S")
        self._updated_at = now.strftime("%H:%M:%S")

        def send(self):

            try:
              if(self._send_at == None):
                from datetime import datetime
                now = datetime.now()
                self._sent_at = now.strftime("%H:%M:%S")

              else:
                raise DataAlreadySent
            except DataAlreadySent as e:
               print("",e)



class DataAlreadySent(Exception):
    pass
