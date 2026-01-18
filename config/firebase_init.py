# import os
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Get absolute path of this file (firebase_init.py)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Build absolute path to serviceAccountKey.json
# KEY_PATH = os.path.join(BASE_DIR, "serviceAccountKey.json")

# cred = credentials.Certificate(KEY_PATH)
# firebase_admin.initialize_app(cred)

# db = firestore.client()

import os, json
import firebase_admin
from firebase_admin import credentials, firestore

cred_dict = json.loads(os.environ["FIREBASE_KEY"])
cred = credentials.Certificate(cred_dict)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

