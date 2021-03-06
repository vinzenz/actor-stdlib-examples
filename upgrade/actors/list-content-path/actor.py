import subprocess

from leapp.actors import Actor
from leapp.models import LanguagePaths, LanguagePackagePaths
from leapp.tags import IPUTag, FactsTag


COMMAND_TMPL = "find -P {path} -maxdepth 0 -type d 2> /dev/null"


class ListContentPath(Actor):
    name = 'list-content-path'
    description = 'For the actor list-content-path has been no description provided.'
    consumes = (LanguagePaths,)
    produces = (LanguagePackagePaths,)
    tags = (IPUTag, FactsTag)

    def process(self):
        for message in self.consume():
            paths = []

            for path in message.paths:
                paths.extend(
                    subprocess.check_output(COMMAND_TMPL.format(path=path), shell=True).rstrip().split('\n')
                )

            self.produce(LanguagePackagePaths(paths=paths, context=message.context))
