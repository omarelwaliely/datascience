import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity[['player_id','event_date']].sort_values(by = 'event_date', ascending = True).drop_duplicates(subset = ['player_id']).rename(columns = {'event_date':'first_login'})