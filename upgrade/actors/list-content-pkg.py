import subprocess

from leapp.actors import Actor
from leapp.models import LanguagePackagePaths, RHPackages, CheckOutput

COMMAND_TMPL = "rpm -qf {content}"

class ListContentPkg(Actor):
    name = 'list-content-pkg'
    description = '''
        List which RPM package provides content provided as input or add
        any found issue to check_output message channel
    '''
    consumes = (LanguagePackagePaths,)
    produces = (RHPackages,CheckOutput)
    tags = ('ipu', 'facts')

    def process(self):
        for message in self.consume():
            not_packaged = set()
            packages = set()
            for path in message.paths:
                try:
                    packages.add(subprocess.check_output(COMMAND_TMPL.format(content=path)).rstrip())
                except subprocess.CalledProcessError:
                    not_packaged.add(path)
            if packages:
                self.produce(
                    RHPackages(
                        packages=list(packages),
                        context=message.context))

            if not_packaged:
                self.produce(
                    CheckOutput(
                        check_actor=self.name,
                        check_action=message.context,
                        status='FAIL',
                        summary='Path is not owned by any package',
                        params=list(not_packaged)))
