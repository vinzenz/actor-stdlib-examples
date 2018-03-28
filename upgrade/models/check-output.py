from leapp.models import Model, fields

from leapp.topics import CheckOutputTopic


class CheckOutput(Model):
    topic = CheckOutputTopic
    check_actor = fields.String(required=True)
    check_action = fields.String()
    status = fields.String(required=True)
    summary = fields.String(required=True)
    params = fields.List(fields.String(), required=True)

