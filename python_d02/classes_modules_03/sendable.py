from datetime import datetime
now = datetime.now()


class Sendable:
    def __init__(self,_body, _subject, _from, _to,_Dictionary, _sent_at=None):

        self._body =_body
        self._subject =_subject
        self._from =_from
        self._to = _to
        self._Dictionary = _Dictionary
        self._created_at = now.strftime("%H:%M:%S")
        self._updated_at = now.strftime("%H:%M:%S")


    def send(self):

        try:
            if(self._send_at is None):
                from datetime import datetime
                now = datetime.now()
                self._sent_at = now.strftime("%H:%M:%S")
                self._Dictionary={}
                dico=[self._from,self._to,self._send_at]
                self._Dictionary = dico
            else:
                raise DataAlreadySent
        except DataAlreadySent as e:
            print("",e)


    def history(self):
        items = self._Dictionary.items()
        return items




class DataAlreadySent(Exception):
    pass



#m=Sendable("body", "sujet", "moi", "toi","epitech,to,sam")

#print(m._body, m._subject, m._from, m._to, m._created_at, m._updated_at)
#print(m._Dictionary)
