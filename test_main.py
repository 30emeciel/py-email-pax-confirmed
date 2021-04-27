from unittest import TestCase

import dotenv
from box import Box


class Test(TestCase):

    def setUp(self) -> None:
        dotenv.load_dotenv()

    def test_trigger_on_update_pax(self):
        import main
        doc_path = "pax/auth0|5ff87d92a54dd0006f957407"
        event = {
          "oldValue": {
            "createTime": "2021-03-05T19:54:37.991311Z",
            "fields": {
              "arrival_date": { "timestampValue": "2021-03-15T23:00:00Z" },
              "created": { "timestampValue": "2021-03-05T19:54:37.978Z" },
              "departure_date": { "timestampValue": "2021-03-19T23:00:00Z" },
              "kind": { "stringValue": "COLIVING" },
              "number_of_nights": { "integerValue": "4" },
              "state": { "stringValue": "PENDING_REVIEW" }
            },
            "name": f"projects/trentiemeciel/databases/(default)/documents/{doc_path}",
            "updateTime": "2021-03-05T21:56:55.248879Z"
          },
          "updateMask": { "fieldPaths": ["state"] },
          "value": {
            "createTime": "2021-03-05T19:54:37.991311Z",
            "fields": {
              "arrival_date": { "timestampValue": "2021-03-15T23:00:00Z" },
              "created": { "timestampValue": "2021-03-05T19:54:37.978Z" },
              "departure_date": { "timestampValue": "2021-03-19T23:00:00Z" },
              "kind": { "stringValue": "COLIVING" },
              "number_of_nights": { "integerValue": "4" },
              "state": { "stringValue": "CANCELED" }
            },
            "name": f"projects/trentiemeciel/databases/(default)/documents/{doc_path}",
            "updateTime": "2021-03-05T21:56:55.248879Z"
          }
        }

        main.trigger_on_update_pax(doc_path=doc_path, event=Box(event))

