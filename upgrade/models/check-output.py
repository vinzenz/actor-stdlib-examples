from leapp.models import Model, fields

from upgrade.channels import CheckOutputChannel


class CheckOutput(Model):
    channel = CheckOutputChannel
    check_actor = fields.String(required=True)
    check_action = fields.String()
    status = fields.String(required=True)
    summary = fields.String(required=True)
    params = fields.List(fields.String)

