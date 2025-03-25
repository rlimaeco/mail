# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _notify_compute_recipients(self, message, msg_vals):
        recipients = super()._notify_compute_recipients(message, msg_vals)
        # The context key `force_notification_by_email` allows to
        # push notifications through email even if the user has his preferences
        # configured to use Odoo.
        if self.env.context.get("force_notification_by_email"):
            for partner in recipients.get("partners", []):
                partner["notif"] = "email"
        return recipients
