import pandas as pd
import os
from questions_preparation import PrepareClosedEndedQuestions

os.chdir("../")

no_precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="reszta")
precambr_data = pd.read_excel(f"{os.getcwd()}\inputs\wucziapping_data.xlsx", sheet_name="Prekambr")

test1 = PrepareClosedEndedQuestions(1, 3, 10)
questhard1 = test1.prepare_questions(False, no_precambr_data, precambr_data, "SYSTEM", "PIETRO", "Wybierz piętro systemu", True)
test1 = PrepareClosedEndedQuestions(1, 3, 3)
questeasy1 = test1.prepare_questions(False, no_precambr_data, precambr_data, "SYSTEM", "PIETRO", "Wybierz piętro systemu", False)

test2 = PrepareClosedEndedQuestions(2, 3, 10)
questhard2 = test2.prepare_questions(False, no_precambr_data, precambr_data, "ODDZIAL", "PIETRO", "Wybierz piętro oddziału", True)
test2 = PrepareClosedEndedQuestions(2, 3, 3)
questeasy2 = test2.prepare_questions(False, no_precambr_data, precambr_data, "ODDZIAL", "PIETRO", "Wybierz piętro oddziału", False)

test3 = PrepareClosedEndedQuestions(1, 2, 10)
questhard3 = test3.prepare_questions(False, no_precambr_data, precambr_data, "SYSTEM", "ODDZIAL", "Wybierz oddział systemu", True)
test3 = PrepareClosedEndedQuestions(1, 2, 3)
questeasy3 = test3.prepare_questions(False, no_precambr_data, precambr_data, "SYSTEM", "ODDZIAL", "Wybierz oddział systemu", False)

test4 = PrepareClosedEndedQuestions(0, 1, 10)
questhard4 = test4.prepare_questions(False, no_precambr_data, precambr_data, "ERA", "SYSTEM", "Wybierz system ery", True)
test4 = PrepareClosedEndedQuestions(0, 1, 3)
questeasy4 = test4.prepare_questions(False, no_precambr_data, precambr_data, "ERA", "SYSTEM", "Wybierz system ery", False)

test5 = PrepareClosedEndedQuestions(2, 3, 3)
questhard5 = test5.prepare_questions(True, no_precambr_data, precambr_data, "Era", "System", "Prekambr - wybierz system ery", True)
test5 = PrepareClosedEndedQuestions(2, 3, 2)
questeasy5 = test5.prepare_questions(True, no_precambr_data, precambr_data, "Era", "System", "Prekambr - wybierz system ery", False)

test6 = PrepareClosedEndedQuestions(1, 2, 3)
questhard6 = test6.prepare_questions(True, no_precambr_data, precambr_data, "Eon", "Era", "Prekambr - wybierz erę eonu", True)
test6 = PrepareClosedEndedQuestions(1, 2, 2)
questeasy6 = test6.prepare_questions(True, no_precambr_data, precambr_data, "Eon", "Era", "Prekambr - wybierz erę eonu", False)

test7 = PrepareClosedEndedQuestions(1, 3, 3)
questhard7 = test6.prepare_questions(True, no_precambr_data, precambr_data, "Eon", "System", "Prekambr - wybierz system eonu", True)
test7 = PrepareClosedEndedQuestions(1, 3, 2)
questeasy7 = test6.prepare_questions(True, no_precambr_data, precambr_data, "Eon", "System", "Prekambr - wybierz system eonu", False)

all_questions = [
    questhard1,
    questeasy1,
    questhard2,
    questeasy2,
    questhard3,
    questeasy3,
    questhard4,
    questeasy4,
    questhard5,
    questeasy5,
    questhard6,
    questeasy6,
    questhard7,
    questeasy7,
]

df = pd.concat(
    all_questions,
    axis=0
)

print(df)