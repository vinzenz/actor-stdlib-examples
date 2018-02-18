from leapp.models import Model, fields

from upgrade.channels import SystemInfoChannel


class LanguagePaths(Model):
    channel = SystemInfoChannel
    paths = fields.List(fields.String, required=True)
    context = fields.String(required=True)


class LanguagePackagePaths(Model):
    channel = SystemInfoChannel
    paths = fields.List(fields.String, required=True)
    context = fields.String(required=True)


class RHPackages(Model):
    channel = SystemInfoChannel
    packages = fields.List(fields.String, required=True)
    context = fields.String(required=True)
