from leapp.models import Model, fields
from leapp.channels import CabalChannel

class Message(Model):
    channel = CabalChannel
    context = fields.String(required=True, default='Cabal')
    message = fields.String(required=True, default='Some stupid message')
    random = fields.String()
