import pandas as pd
import numpy as np

def make_db_tables_from_df_closed_ended(df:pd.DataFrame):

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
    correct_ans = df['correct_answer']\
        .drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'correct_answer_key'})
    correct_ans['correct_answer_key'] = np.arange(1, len(correct_ans)+1)
    df=pd.merge(df, correct_ans, how='left', on='correct_answer').drop(columns='correct_answer')

    # isMulti
    is_multi_df = df['isMulti'].drop_duplicates().to_frame()\
        .reset_index()\
        .rename(columns={'index':'is_multi_key'})
    is_multi_df['is_multi_key'] = np.arange(1,len(is_multi_df)+1)

    df = pd.merge(df, is_multi_df, how='left', on='isMulti').drop(columns='isMulti')
    
    return df, categories, possible_answers, question_txt, correct_ans, is_multi_df

def make_db_tables_from_df_open_ended(df:pd.DataFrame):

    # categories
    df['category'] = df['question'].str.split().str[:3].str.join(" ")
    categories = df['category'].drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'category_key'})
    categories['category_key'] = np.arange(1, len(categories)+1)
    df = pd.merge(df, categories, how='left', on='category').drop(columns='category')

    #scopes
    scopes_df = df['scope'].drop_duplicates()\
        .drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'scope_key'})
    scopes_df['scope_key'] = np.arange(1, len(scopes_df)+1)
    df = pd.merge(df, scopes_df, how='left', on='scope').drop(columns='scope')

    # wrong scopes
    wrong_scopes_df = df['wrongScope'].drop_duplicates()\
        .drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'wrong_scope_key'})
    wrong_scopes_df['wrong_scope_key'] = np.arange(1, len(wrong_scopes_df)+1)
    df = pd.merge(df, wrong_scopes_df, how='left', on='wrongScope').drop(columns='wrongScope')

    # question txt
    quest_txt_df = df['question'].drop_duplicates()\
        .drop_duplicates()\
        .to_frame()\
        .reset_index()\
        .rename(columns={'index':'quest_txt_key'})
    quest_txt_df['quest_txt_key'] = np.arange(1, len(quest_txt_df)+1)
    df = pd.merge(df, quest_txt_df, how='left', on='question').drop(columns='question')

    return df, categories, scopes_df, wrong_scopes_df, quest_txt_df


class DataFrameToDatabaseTables:

    def __init__(self, inputDataFrame:pd.DataFrame):
        self.inputDataFrame = inputDataFrame

    def prepare_closed_ended_tables(self):
        pass

    def prepare_open_ended_tables(self, *colNames):
        data = self.inputDataFrame
        data['category'] = data['question'].str.split().str[:3].str.join(" ")
        col_names_list = ['category'] + list(colNames)
        dfs_out = []
        for col in col_names_list:
            new_main_df, temp_rel_df = self.make_relation(data, col)
            data = new_main_df
            dfs_out.append(temp_rel_df)
        return data, dfs_out

    @staticmethod
    def make_relation(df, colName):
        rel_df = df[colName].drop_duplicates()\
            .drop_duplicates()\
            .to_frame()\
            .reset_index()\
            .rename(columns={'index':f'{colName}_key'})
        rel_df[f'{colName}_key'] = np.arange(1, len(rel_df)+1)
        df = pd.merge(df, rel_df, how='left', on=colName).drop(columns=colName)

        return df, rel_df