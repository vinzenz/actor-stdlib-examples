import subprocess

from leapp.actors import Actor
from leapp.models import CheckOutput, RHPackages


RHSIGN = ["199e2f91fd431d51",
          "5326810137017186",
          "938a80caf21541eb",
          "fd372689897da07a",
          "45689c882fa658e0"]

COMMAND_TMPL = "rpm -q --qf '%{{SIGPGP:pgpsig}}\n' {pkg}"

class VerifyPkgRhsigned(Actor):
    name = 'verify-pkg-rhsigned'
    description = 'For the actor verify-pkg-rhsigned has been no description provided.'
    consumes = (RHPackages,)
    produces = (CheckOutput,)
    tags = ('ipu', 'checks')

    def process(self):
        for message in self.consume():
            not_signed = set()
            for package in message.packages:
                out = subprocess.check_output(COMMAND_TMPL.format(pkg=package, shell=True))
                for sign in RHSIGN:
                    if sign in out:
                        break
                else:
                    not_signed.add(package)

            self.produce(CheckOutput(
                check_actor=self.name,
                check_action=message.context,
                status='FAIL',
                summary='Package is not signed by Red Hat',
                params=list(not_signed)
            ))
