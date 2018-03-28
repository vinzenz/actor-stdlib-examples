from leapp.actors import Actor
from leapp.models import CheckOutput
from leapp.tags import IPUTag, ReportTag

from pprint import pformat

class Reporttest(Actor):
    name = 'reporttest'
    description = 'For the actor reporttest has been no description provided.'
    consumes = (CheckOutput,)
    produces = ()
    tags = (IPUTag, ReportTag)

    def process(self):
        self.log.info('output: %s', pformat(list(item.dump() for item in self.consume(CheckOutput)), ))
