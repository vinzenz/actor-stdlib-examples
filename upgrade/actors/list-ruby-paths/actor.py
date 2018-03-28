from leapp.actors import Actor
from leapp.models import LanguagePaths
from leapp.tags import IPUTag, FactsTag


class ListRubyPaths(Actor):
    name = 'list-ruby-paths'
    description = 'For the actor list-ruby-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = (IPUTag, FactsTag)

    def process(self):
        self.produce(
            LanguagePaths(
                paths=['/usr/lib/ruby/site_ruby/*/*', '/usr/lib/ruby/gems/*/gems/*'],
                context='Ruby'))
