from leapp.actors import Actor
from leapp.models import CheckOutput
from leapp.tags import IPUTag, FactsTag

from pprint import pprint

class Reporttest(Actor):
    name = 'reporttest'
    description = 'For the actor reporttest has been no description provided.'
    consumes = (CheckOutput,)
    produces = ()
    tags = (IPUTag, FactsTag)

    def process(self):
        pprint(list(CheckOutput.__schema__().dump(item).data for item in self.consume(CheckOutput)))
