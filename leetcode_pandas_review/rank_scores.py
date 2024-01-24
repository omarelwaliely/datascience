import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)
    return scores.drop(columns = ['id']).sort_values(by = ['score'], ascending = False)