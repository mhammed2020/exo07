import os
import random
decks: Optional[Dict[str, Deck]] = None

def get_decks() -> Dict[str, Deck]:
    global decks
    if decks is None:
        random.seed(os.environ.get("DEAL_APP_SEED"))
        # Database connection might go here.
        decks = {}
    return decks