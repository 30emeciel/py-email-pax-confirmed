import logging
import os

import firebase_admin
from box import Box
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
from jinja2 import Environment, FileSystemLoader, select_autoescape

from mail import send_mail
from rst import generate_confirmed_pax_html_text, generate_confirmed_pax_title

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': "trentiemeciel",
})

logging.basicConfig(level=os.environ.get("LOGGING_LEVEL", "DEBUG"))

log = logging.getLogger(__name__)
db = firestore.client()

env = Environment(
    loader=FileSystemLoader("res"),
    autoescape=select_autoescape(['html', 'xml'])
)


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

    data = Box({
        "pax": pax
    })
    html = generate_confirmed_pax_html_text(data)
    title = generate_confirmed_pax_title(data)

    send_mail(pax.email, title, html)

