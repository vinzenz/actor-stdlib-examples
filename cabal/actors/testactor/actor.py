from leapp.actors import Actor
from leapp.models import Message
from leapp.channels import CabalChannel

class Testactor(Actor):
    name = 'testactor'
    description = 'For the actor testactor has been no description provided.'
    consumes = CabalChannel.messages
    produces = (Message,)
    tags = ('test',)

    def process(self):
        for entry in self.consume():
            entry.message
            entry.context
        self.produce(Message())
        self.produce(Message(random='Random value'))
        msg = Message()
        msg.random = 'Whatever'
        self.produce(msg)
