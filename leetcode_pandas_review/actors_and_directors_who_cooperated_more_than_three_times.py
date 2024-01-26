import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id','director_id']).agg(count=('timestamp', 'nunique')).reset_index()
    return result[result['count'] >=3][['actor_id','director_id']]