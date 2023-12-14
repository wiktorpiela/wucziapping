import pandas as pd
import numpy as np

def make_db_tables_from_df(df:pd.DataFrame):

    # make category table and relation ----------
    df['category']=df['question'].str.split().str[:3].str.join(" ")
    categories=df['category'].drop_duplicates().to_frame().reset_index(drop=True)
    categories['category_key'] = np.arange(1,len(categories)+1)
    df = pd.merge(df, categories, how='left', on='category').drop(columns='category')

    #possible answers ------------------
    cols = ['A','B','C','D','E','F','G','H','I']
    possible_answers = df[cols]\
        .reset_index()\
        .rename(columns={'index':'possible_answers_key'})
    possible_answers['possible_answers_key'] = possible_answers['possible_answers_key']+1
    df.drop(columns=cols, inplace=True)
    df=pd.concat([df, possible_answers['possible_answers_key']], axis=1)

    return df, categories, possible_answers
