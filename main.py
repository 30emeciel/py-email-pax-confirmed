import logging

from box import Box
from core import firestore_client
from core.mailer import Mailer
from core.rst_to_html import to_html
from core.tpl import render

log = logging.getLogger(__name__)

db = firestore_client.db()
mailer = Mailer()


def from_firestore(event, context):
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource

    # print out the resource string that triggered the function
    log.info(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object
    log.debug(str(event))

    trigger_on_update_pax(resource_string, Box(event))


def trigger_on_update_pax(doc_path, event):

    if "state" not in event.updateMask.fieldPaths:
        log.info("state hasn't changed, ignoring")
        return

    pax_ref = db.document(doc_path)
    pax_doc = pax_ref.get()
    assert pax_doc.exists

    pax = Box(pax_doc.to_dict())
    if pax.state != "CONFIRMED":
        log.info(f"pax 'state' != CONFIRMED, ignoring")
        return

    if "email" not in pax:
        log.warning(f"No email field. ignoring pax with id {pax_ref.id} name={pax.name}...")
        return

    data = Box({
        "pax": pax
    })
    html = to_html(render("confirmed_pax_fr.rst", data))
    title = render("confirmed_pax_title_fr.txt", data)

    mailer.send_mail(pax.name, pax.email, title, html)

