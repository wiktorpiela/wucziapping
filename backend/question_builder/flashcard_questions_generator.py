import pandas as pd
import os
from question_builder import QuestionBuilder
from question_utils import DataFrameToDatabaseTables

no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")
test = QuestionBuilder(no_precambr_data, precambr_data)

dfs=[]
criteria=[
    ('non-precambrian', 'oddział', 'ODDZIAL', 'piętro', 'PIETRO', False),
    ('non-precambrian', 'oddział', 'ODDZIAL', 'piętro', 'PIETRO', True),

    ('non-precambrian', 'system', 'SYSTEM', 'piętro', 'PIETRO', False),
    ('non-precambrian', 'system', 'SYSTEM', 'piętro', 'PIETRO', True),

    ('non-precambrian', 'system', 'SYSTEM', 'oddział', 'ODDZIAL', False),
    ('non-precambrian', 'system', 'SYSTEM', 'oddział', 'ODDZIAL', True),

    ('precambrian', ' Prekambr - era', 'ERA', 'system', 'SYSTEM', False),
    ('precambrian', 'Prekambr - era', 'ERA', 'system', 'SYSTEM', True),

    ('precambrian', ' Prekambr - eon', 'Eon', 'era', 'ERA', False),
    # ('precambrian', 'Prekambr - eon', 'Eon', 'era', 'ERA', True),
]

for dataSource, targetName, targetCol, scopeName, scopeCol, is_hard in criteria:

    if is_hard and dataSource!='precambrian':
        iterator = 5
    elif is_hard and dataSource=='precambrian':
        iterator = 2
    else:
        iterator=1

    for i in range(iterator):
        temp = test.prepare_flashcards(dataSource, targetName, targetCol, scopeName, scopeCol, is_hard)
        dfs.append(temp)

df_out = pd.concat(dfs, ignore_index=True).drop_duplicates()
df_out.to_excel(r'outputs/flashcards/wucziapping_question.xlsx', index=False)

df_to_db_obj = DataFrameToDatabaseTables(df_out)
dfs_list = df_to_db_obj.prepare_relational_tables('category', 'scope', 'target_correct', 'target_wrong')

names = ['main_df', 'cat_df', 'scope_df', 'target_df', 'target_wrong_df']

for i in range(len(dfs_list)):
    dfs_list[i].to_csv(fr'outputs/flashcards/{names[i]}.csv', index=False)