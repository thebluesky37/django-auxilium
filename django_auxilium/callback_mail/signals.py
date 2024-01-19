from __future__ import unicode_literals

from django.dispatch import Signal


sending_mail = Signal()
"""
Signal sent when message is being sent.

Parameters
----------
message
    Email message which is being sent
"""
sent_mail = Signal()
"""
Signal sent when message has successfully been sent

Parameters
----------
message
    Email message which was sent
"""
failed_mail = Signal()
"""
Signal sent when message sending has failed

Parameters
----------
message
    Email message which was not sent
reason : str
    Reason for why message was not sent
"""
