import subprocess

from leapp.actors import Actor


COMMAND = "perl -MConfig -e '$,=q{ }; print @Config{installarchlib,installprivlib,installvendorarch,installvendorlib}'"


class ListPerlPaths(Actor):
    name = 'list-perl-paths'
    description = 'For the actor list-perl-paths has been no description provided.'
    consumes = ()
    produces = ()
    tags = ('ipu', 'checks')

    def process(self):
        pass
