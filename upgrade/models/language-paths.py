from leapp.models import Model, fields

from leapp.topics import SystemInfoTopic


class LanguagePaths(Model):
    topic = SystemInfoTopic
    paths = fields.List(fields.String(), required=True)
    context = fields.String(required=True)


class LanguagePackagePaths(Model):
    topic = SystemInfoTopic
    paths = fields.List(fields.String(), required=True)
    context = fields.String(required=True)


class RHPackages(Model):
    topic = SystemInfoTopic
    packages = fields.List(fields.String(), required=True)
    context = fields.String(required=True)
