import pandas as pd
import os
from question_builder import QuestionBuilder
from question_utils import make_db_tables_from_df_open_ended


no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")
test = QuestionBuilder(no_precambr_data, precambr_data)

dfs=[]
criteria=[
    ('non-precambrian', True, 'SYSTEM', 'PIETRO', 'Wypisz piętro systemu'),
    ('non-precambrian', False, 'SYSTEM', 'PIETRO', 'Wypisz piętro systemu'),
    ('non-precambrian', True, 'ODDZIAL', 'PIETRO', 'Wypisz piętro odziału'),
    ('non-precambrian', False, 'ODDZIAL', 'PIETRO', 'Wypisz piętro odziału'),
    ('precambrian', True,  'ERA', 'SYSTEM', 'Wypisz system ery'),
    ('precambrian', False,  'ERA', 'SYSTEM', 'Wypisz system ery'),
    ('precambrian', True, 'Eon', 'ERA', 'Wypisz erę enou'),
    ('precambrian', False, 'Eon', 'ERA', 'Wypisz erę enou'),
]

for dataSource, isClassic, colNameTarget, colNameScope, questionTxt in criteria:
    iterator = 11 if not isClassic else 1
    for i in range(iterator):
        temp = test.prepare_open_ended(dataSource, isClassic, colNameTarget, colNameScope, questionTxt)
        dfs.append(temp)

df_out = pd.concat(dfs, ignore_index=True).drop_duplicates()
df_out.to_excel(r'outputs/open_ended/wucziapping_question.xlsx', index=False)