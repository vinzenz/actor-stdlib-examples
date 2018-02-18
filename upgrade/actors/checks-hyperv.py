import os
import re

from leapp.actors import Actor
from upgrade.models import CheckOutput


class ChecksHyperv(Actor):
    name = 'checks-hyperv'
    description = 'For the actor checks-hyperv has been no description provided.'
    consumes = ()
    produces = (CheckOutput,)
    tags = ('ipu', 'checks')

    def process(self):
        lscpu = os.popen('lscpu').read()
        line = re.search(r"(Hypervisor\s+vendor):\s+(.*)$", lscpu, flags=re.MULTILINE)

        if line:
            vendor = line.group(2)
            if 'Microsoft' in vendor:
                summary = "The system is running as a Hyper-V guest on Microsoft Windows host"
                status = 'FAIL'
            else:
                summary = "The system is running as a virtualized guest"
                status = 'PASS'
        else:
            summary = "System is not virtualized"
            status = 'PASS'
            vendor = ''
        self.produce(CheckOutput(check_actor=self.name, summary=summary, status=status, params=vendor))

