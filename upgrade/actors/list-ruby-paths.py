from leapp.actors import Actor

from upgrade.models import LanguagePaths


class ListRubyPaths(Actor):
    name = 'list-ruby-paths'
    description = 'For the actor list-ruby-paths has been no description provided.'
    consumes = ()
    produces = (LanguagePaths,)
    tags = ('ipu', 'facts')

    def process(self):
        self.produce(
            LanguagePaths(
                path=['/usr/lib/ruby/site_ruby/*/*', '/usr/lib/ruby/gems/*/gems/*'],
                context='Ruby'))
