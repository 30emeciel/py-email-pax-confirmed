from box import Box
from dotenv import load_dotenv

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
    "name": "projects/trentiemeciel/databases/(default)/documents/pax/auth0|5ff87d92a54dd0006f957407",
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
    "name": "projects/trentiemeciel/databases/(default)/documents/pax/auth0|5ff87d92a54dd0006f957407",
    "updateTime": "2021-03-05T21:56:55.248879Z"
  }
}

if __name__ == "__main__":
    load_dotenv()
    from main import trigger_on_update_pax
    trigger_on_update_pax("pax/auth0|5ff87d92a54dd0006f957407", Box(event))

