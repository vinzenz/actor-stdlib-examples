from leapp.models import Model, fields


class CheckOutput(Model):
    check_actor = fields.String(required=True)
    check_action = fields.String()
    status = fields.String(required=True)
    summary = fields.String(required=True)
    params = fields.List(fields.String)

