import pandas as pd
import os
from question_builder import QuestionBuilder
from question_utils import DataFrameToDatabaseTables


no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")
test = QuestionBuilder(no_precambr_data, precambr_data)

dfs=[]
criteria=[
    ('non-precambrian', True, 'SYSTEM', 'PIETRO', 'piętro systemu'),
    ('non-precambrian', False, 'SYSTEM', 'PIETRO', 'piętro systemu'),
    ('non-precambrian', True, 'ODDZIAL', 'PIETRO', 'piętro odziału'),
    ('non-precambrian', False, 'ODDZIAL', 'PIETRO', 'piętro odziału'),
    ('precambrian', True,  'ERA', 'SYSTEM', 'Prekambr - system ery'),
    ('precambrian', False,  'ERA', 'SYSTEM', 'Prekambr - system ery'),
    ('precambrian', True, 'Eon', 'ERA', 'Prekambr - era enou'),
    ('precambrian', False, 'Eon', 'ERA', 'Prekambr - era enou'),
]

for dataSource, isClassic, colNameTarget, colNameScope, questionTxt in criteria:
    iterator = 11 if not isClassic else 1
    for i in range(iterator):
        temp = test.prepare_open_ended(dataSource, isClassic, colNameTarget, colNameScope, questionTxt)
        dfs.append(temp)

df_out = pd.concat(dfs, ignore_index=True).drop_duplicates()
df_out.to_excel(r'outputs/open_ended/wucziapping_question.xlsx', index=False)

df_to_db_obj = DataFrameToDatabaseTables(df_out)
dfs_list = df_to_db_obj.prepare_relational_tables('category', 'target', 'scope', 'wrong_scope')

names = ['main_df', 'cat_df', 'target_df', 'scope_df', 'wrong_scope_df']

for i in range(len(dfs_list)):
    dfs_list[i].to_csv(fr'outputs/open_ended/{names[i]}.csv', index=False)