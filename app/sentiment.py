from .afinn import Afinn
import re


def sentiment_score(tweet):
    afinn_ = Afinn()
    res = re.sub(r'[^a-zA-Z]', ' ', tweet)
    res = res.lower()
    res = res.strip()
    try:
        return int(afinn_.score(res))
    except Exception:
        return 0
