import pandas as pd
import numpy as np
import os
from question_builder import QuestionBuilder
from question_utils import DataFrameToDatabaseTables

no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")

questions = QuestionBuilder(no_precambr_data, precambr_data)

dfs = []
criteria = [
    (False, True, True, 1, 9, "ERA", "SYSTEM", "system ery", True, []),
    (False, True, False, 1, 9, "ERA", "PIETRO", "piętro ery", True, []),
    (False, False, False, 3, 6, "SYSTEM", "ODDZIAL", "oddział systemu", True, ['kreda','jura','trias','dewon','ordowik']),
    (False, True, False, 1, 9, "SYSTEM", "PIETRO", "piętro systemu", True, []),
    (False, True, False, 1, 9, "ODDZIAL", "PIETRO", "piętro oddziału", False, []),
    (True, True, True, 1, 9, "ERA", "SYSTEM", "Prekambr - system ery", True, ['neoarchaik','mezoarchaik','paleoarchaik','eoarchaik','brak']),
]

for is_prek, if_multi, both_scopes, multiplyIdx, possAns, targetName, scopeName, questionTxt, excludeEmpty, explusionList in criteria:
    temp = questions.prepare_closed_ended(is_prek, if_multi, both_scopes, multiplyIdx, possAns, targetName, scopeName, questionTxt, excludeEmpty, explusionList)

    if if_multi:
        temp['is_multi']=1
    else:
        temp['is_multi']=0

    dfs.append(temp)

df_final = pd.concat(dfs)
df_final.to_excel(r'outputs/wucziapping_question.xlsx', index=False)

test = DataFrameToDatabaseTables(df_final)
df_list = test.prepare_relational_tables('category', 'target', 'possible_answers', 'correct_answer', 'is_multi')
names = ['main_df', 'cat_df', 'target_df', 'possible_answers_df', 'correct_answer_df', 'is_multi']
for i in range(len(df_list)):
    df_list[i].to_csv(fr'outputs/closed_ended/{names[i]}.csv', index=False)

