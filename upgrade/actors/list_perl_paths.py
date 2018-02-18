import subprocess

from leapp.actors import Actor
from upgrade.models import LanguagePaths

COMMAND = "perl -MConfig -e '$,=q{ }; print @Config{installarchlib,installprivlib,installvendorarch,installvendorlib}'"


class ListPerlPaths(Actor):
    name = 'list-perl-paths'
    description = 'For the actor list-perl-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = ('ipu', 'facts')

    def process(self):
        self.produce(
            LanguagePaths(
                paths=subprocess.check_output(COMMAND, shell=True).rstrip().split(' '),
                context='Perl'))
