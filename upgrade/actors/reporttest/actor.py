from leapp.actors import Actor
from leapp.models import CheckOutput
from leapp.tags import IPUTag, ReportTag

from leapp.libraries.common.upgrade import NAME
from leapp.libraries.common import upgrade, test
from pprint import pformat

class Reporttest(Actor):
    name = 'reporttest'
    description = 'For the actor reporttest has been no description provided.'
    consumes = (CheckOutput,)
    produces = ()
    tags = (IPUTag, ReportTag)

    def process(self):
        self.log.info('output: %s', pformat(list(CheckOutput.__schema__().dump(item).data for item in self.consume(CheckOutput)), ))
        self.log.info('Common upgrade library name: "%s"/"%s", %d', NAME, upgrade.NAME, test.WOOT)
