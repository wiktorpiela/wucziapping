import pandas as pd
import numpy as np
import os
from question_builder import QuestionBuilder
from question_utils import make_db_tables_from_df

no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")

questions = QuestionBuilder(no_precambr_data, precambr_data)

dfs = []
criteria = [
    (False, True, True, 1, 9, "ERA", "SYSTEM", "Wybierz system ery", True, []),
    (False, True, False, 1, 9, "ERA", "PIETRO", "Wybierz piętro ery", True, []),
    (False, False, False, 3, 6, "SYSTEM", "ODDZIAL", "Wybierz oddział systemu", True, ['kreda','jura','trias','dewon','ordowik']),
    (False, True, False, 1, 9, "SYSTEM", "PIETRO", "Wybierz piętro systemu", True, []),
    (False, True, False, 1, 9, "ODDZIAL", "PIETRO", "Wybierz piętro oddziału", False, []),
    (True, True, True, 1, 9, "ERA", "SYSTEM", "Wybierz system ery", True, ['neoarchaik','mezoarchaik','paleoarchaik','eoarchaik','brak']),
]

for is_prek, if_multi, both_scopes, multiplyIdx, possAns, targetName, scopeName, questionTxt, excludeEmpty, explusionList in criteria:
    temp = questions.prepare_closed_ended(is_prek, if_multi, both_scopes, multiplyIdx, possAns, targetName, scopeName, questionTxt, excludeEmpty, explusionList)

    if if_multi:
        temp['isMulti']=1
    else:
        temp['G'] = np.nan
        temp['H'] = np.nan
        temp['I'] = np.nan
        temp['isMulti']=0

    dfs.append(temp)

df_final = pd.concat(dfs)
df_final.to_excel(r'outputs/wucziapping_question.xlsx', index=False)

dfs_to_db = make_db_tables_from_df(df_final)
names = ["main_df", "cat_df", "pos_ans_df", "q_txt_df", "corr_ans_df", "is_multi_df"]

for i in range(len(dfs_to_db)):
    dfs_to_db[i].to_csv(fr'outputs/{names[i]}.csv', index=False)

