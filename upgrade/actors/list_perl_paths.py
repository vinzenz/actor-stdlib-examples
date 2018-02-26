import subprocess

from leapp.actors import Actor
from leapp.models import LanguagePaths
from leapp.tags import IPUTag, FactsTag

COMMAND = "perl -MConfig -e '$,=q{ }; print @Config{installarchlib,installprivlib,installvendorarch,installvendorlib}'"


class ListPerlPaths(Actor):
    name = 'list-perl-paths'
    description = 'For the actor list-perl-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = (IPUTag, FactsTag)

    def process(self):
        self.produce(
            LanguagePaths(
                paths=subprocess.check_output(COMMAND, shell=True).rstrip().split(' '),
                context='Perl'))
