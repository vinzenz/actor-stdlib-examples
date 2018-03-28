import re
import subprocess

from leapp.libraries.actor.foo import NAME as FOO_NAME
from leapp.libraries.actor.foo import bar
from leapp.libraries.actor.foo.bar import NAME as BAR_NAME
from leapp.libraries.actor import test

from leapp.actors import Actor
from leapp.models import CheckOutput
from leapp.tags import IPUTag, FactsTag

class ChecksHyperv(Actor):
    name = 'checks-hyperv'
    description = 'For the actor checks-hyperv has been no description provided.'
    consumes = ()
    produces = (CheckOutput,)
    tags = (IPUTag, FactsTag)

    def process(self):
        lscpu = subprocess.check_output('lscpu', shell=True)
        line = re.search(r"(Hypervisor\s+vendor):\s+(.*)$", lscpu, flags=re.MULTILINE)

        output = CheckOutput(check_actor=self.name, status='PASS', params=[], summary='')
        if line:
            output.params = [line.group(2)]
            if 'Microsoft' in output.params:
                output.summary = "The system is running as a Hyper-V guest on Microsoft Windows host"
                output.status = 'FAIL'
            else:
                output.summary = "The system is running as a virtualized guest"
        else:
            output.summary = "System is not virtualized"

        self.produce(output)
        self.produce(output)
        self.log.info("ChecksHyperv dared to log something")
        self.log.info("Well we imported, foo.NAME = %s, bar.NAME = %s, BAR_NAME = %s, test.NAME = %s", FOO_NAME, bar.NAME, BAR_NAME, test.NAME)

