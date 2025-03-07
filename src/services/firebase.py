from firebase_admin import credentials, auth, initialize_app

cred = credentials.Certificate("/src/services/firebase-services.json")

# Initialize Firebase Admin SDK 
# with the credentials
initialize_app(cred)

def verify_id_token(token: str) -> dict:
    return auth.verify_id_token(
        token, 
        check_revoked=True
    )
