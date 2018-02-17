from leapp.channels import Channel
from upgrade.models import CheckOutput

class CheckOutputChannel(Channel):
    name = 'check-output'
    messages = (CheckOutput,)
