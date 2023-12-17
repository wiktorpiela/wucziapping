import pandas as pd
import numpy as np

def make_db_tables_from_df(df:pd.DataFrame):

    # make category table and relation ----------
    df['category']=df['question'].str.split().str[:3].str.join(" ")
    categories=df['category'].drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'category_key'})
    categories['category_key'] = np.arange(1,len(categories)+1)
    df = pd.merge(df, categories, how='left', on='category').drop(columns='category')

    # possible answers ------------------
    cols = ['A','B','C','D','E','F','G','H','I']
    possible_answers = df[cols]\
        .reset_index()\
        .rename(columns={'index':'possible_answers_key'})
    possible_answers['possible_answers_key'] = possible_answers['possible_answers_key']+1
    df.drop(columns=cols, inplace=True)
    df=pd.concat([df, possible_answers['possible_answers_key']], axis=1)

    # question text --------------------------
    question_txt = df['question'].drop_duplicates()\
        .reset_index()\
        .rename(columns={'index':'question_txt'})
    question_txt['question_txt'] = np.arange(1, len(question_txt)+1)
    df=pd.merge(df, question_txt, how='left', on='question').drop(columns='question')

    # correct answers ------------------------
    correct_ans = df['correct_answer'].to_frame().reset_index(drop=True)
    correct_ans['uni'] = correct_ans['correct_answer'].str.join('')
    uni_df = correct_ans['uni'].to_frame().drop_duplicates().reset_index()
    uni_idx = uni_df['index'].values
    correct_ans=correct_ans.reset_index()
    correct_ans = correct_ans[correct_ans['index'].isin(uni_idx)]
    correct_ans['index']=np.arange(1, len(correct_ans)+1)
    correct_ans.rename(columns={'index':'correct_answer_key'}, inplace=True)

    df['corr_ans_key'] = df['correct_answer'].str.join('')
    df = pd.merge(df, correct_ans[['correct_answer_key','uni']], how='left', left_on='corr_ans_key', right_on='uni')\
        .drop(columns=['correct_answer','corr_ans_key','uni'])
    
    correct_ans = correct_ans[['correct_answer_key','correct_answer']]
    correct_ans=correct_ans.explode('correct_answer')

    # isMulti
    is_multi_df = df['isMulti'].drop_duplicates().to_frame()\
        .reset_index()\
        .rename(columns={'index':'is_multi_key'})
    is_multi_df['is_multi_key'] = np.arange(1,len(is_multi_df)+1)

    df = pd.merge(df, is_multi_df, how='left', on='isMulti').drop(columns='isMulti')
    
    return df, categories, possible_answers, question_txt, correct_ans, is_multi_df
