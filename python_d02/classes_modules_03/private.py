from sendable import Sendable

class Private(Sendable):

    def send(self):


            if(self._send_at is None):
                self._Dictionary={}
                dico=[self._from,self._to,self._send_at]
                self._Dictionary = dico
            else:
                print("already sent")

