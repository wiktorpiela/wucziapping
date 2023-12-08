import pandas as pd
import os
from question_builder import QuestionBuilder

# os.chdir("../")

no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")

questions = QuestionBuilder(no_precambr_data, precambr_data)

dfs = []
criteria = [
    # NON PRECAMBRIAN
    # era
    (False, False, 3, "ERA", "SYSTEM", "Wybierz system ery"),
    (False, True, 15, "ERA", "SYSTEM", "Wybierz system ery"),
    (False, False, 3, "ERA", "ODDZIAL", "Wybierz oddział ery"),
    (False, True, 15, "ERA", "ODDZIAL", "Wybierz oddział ery"),
    (False, False, 3, "ERA", "PIETRO", "Wybierz piętro ery"),
    (False, True, 15, "ERA", "PIETRO", "Wybierz piętro ery"),
    # system
    (False, False, 3, "SYSTEM", "ODDZIAL", "Wybierz oddział systemu"),
    (False, True, 15, "SYSTEM", "ODDZIAL", "Wybierz oddział systemu"),
    (False, False, 3, "SYSTEM", "PIETRO", "Wybierz piętro systemu"),
    (False, True, 15, "SYSTEM", "PIETRO", "Wybierz piętro systemu"),
    # oddział
    (False, False, 3, "ODDZIAL", "PIETRO", "Wybierz piętro oddziału"),
    (False, True, 15, "ODDZIAL", "PIETRO", "Wybierz piętro oddziału"),

    ## PRECAMBRIAN
    # prekambr
    (True, False, 2, "Jednostka nieformalna", "Eon", "Prekambr - Wybierz eon prekambru"), #not exist for single
    (True, True, 10, "Jednostka nieformalna", "Eon", "Prekambr - Wybierz eon prekambru"),
    (True, False, 2, "Jednostka nieformalna", "Era", "Prekambr - Wybierz erę prekambru"), #not exist for single
    (True, True, 10, "Jednostka nieformalna", "Era", "Prekambr - Wybierz erę prekambru"),
    (True, False, 2, "Jednostka nieformalna", "System", "Prekambr - Wybierz system prekambru"), #not exist for single
    (True, True, 10, "Jednostka nieformalna", "System", "Prekambr - Wybierz system prekambru"),
    # eon
    (True, False, 2, "Eon", "Era", "Prekambr - Wybierz erę enou"),
    (True, True, 10, "Eon", "Era", "Prekambr - Wybierz erę enou"),
    (True, False, 2, "Eon", "System", "Prekambr - Wybierz system enou"), #!!!!! manual for single
    (True, True, 10, "Eon", "System", "Prekambr - Wybierz system enou"),
    # system ery
    (True, False, 2, "Era", "System", "Prekambr - Wybierz system ery"),
    (True, True, 10, "Era", "System", "Prekambr - Wybierz system ery"),
]

for is_prek, is_hard, coeff, key1, key2, quest_txt in criteria:
    quest = questions.prepare_multi(is_prek, coeff, key1, key2, quest_txt)
    dfs.append(quest)
    print(f"{is_prek} {is_hard} {coeff} {key1}, {key2}, {quest_txt}")

df_final = pd.concat(dfs)
df_final.to_csv(fr'{os.getcwd()}\outputs\precambrian_questions_multi.csv', index=False)



