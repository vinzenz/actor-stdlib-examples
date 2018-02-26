from leapp.actors import Actor
from leapp.models import LanguagePaths
from leapp.tags import IPUTag, FactsTag


class ListPythonPaths(Actor):
    name = 'list-python-paths'
    description = 'For the actor list-python-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = (IPUTag, FactsTag)

    def process(self):
        self.produce(
            LanguagePaths(
                paths=["/usr/lib*/python*/site-packages/*"], context="Python"))
