from leapp.actors import Actor

from upgrade.models import LanguagePaths


class ListPythonPaths(Actor):
    name = 'list-python-paths'
    description = 'For the actor list-python-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = ('ipu', 'facts')

    def process(self):
        self.produce(
            LanguagePaths(
                paths=["/usr/lib*/python*/site-packages/*"], context="Python"))
