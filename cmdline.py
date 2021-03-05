import logging

from dotmap import DotMap

log = logging.getLogger(__name__)

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    # export GOOGLE_APPLICATION_CREDENTIALS="trentiemeciel.json"
    # get the token using postman
    import main
    data = {}
    path = '/pax/auth0|5ff87d92a54dd0006f957407/requests/J1pmkMNjGEpHc5qUUQ5m'
    context = DotMap({
        "resource": f'projects/trentiemeciel/databases/(default)/documents{path}'
    })
    main.from_firestore(data, context)
