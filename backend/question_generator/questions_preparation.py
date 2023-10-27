import pandas as pd
import numpy as np

class PrepareClosedEndedQuestions:

    def __init__(self, startColIdx:int, endColIdx:int, multiplyRowsIdx:int):
        self.startColIdx = startColIdx
        self.endColIdx = endColIdx
        self.multiplyRowsIdx = multiplyRowsIdx

    def prepare_questions(self, isPrekambr:bool, inputData:pd.DataFrame, inputDataPrekambr:pd.DataFrame, colName1:str, colName2:str, questionPattern:str, isHard:bool):
        data = inputData
        dataPrekambr = inputDataPrekambr

        if isPrekambr:
            df = dataPrekambr.iloc[:, [self.startColIdx,self.endColIdx]]
        else:
            df = data.iloc[:, [self.startColIdx,self.endColIdx]]

        df = df.loc[df.index.repeat(self.multiplyRowsIdx)]

        random_answers = []
        questions = []

        if isHard:
            scope = np.unique(
                        np.concatenate((data["PIETRO"].unique(), data["ODDZIAL"].unique(), data["SYSTEM"].unique(), data["ERA"].unique(), 
                                dataPrekambr["Jednostka nieformalna"].unique(), dataPrekambr["Eon"].unique(), 
                                dataPrekambr["Era"].unique(), dataPrekambr["System"].unique()))
                                )

        else:
            if isPrekambr:
                scope = dataPrekambr[colName2].unique()
            else:
                scope = data[colName2].unique()

        for i in df[colName1]:
            if isPrekambr:
                temp_correct = dataPrekambr[dataPrekambr[colName1]==i][colName2].array
            else:
                temp_correct = data[data[colName1]==i][colName2].array

            indexes = np.nonzero(np.in1d(scope, temp_correct))[0]
            temp_scope = np.delete(scope, indexes)
            
            if isHard:
                temp = np.concatenate((np.random.choice(temp_scope,4), np.random.choice(temp_correct,1)))
            else:
                temp = np.concatenate((np.random.choice(temp_scope,3), np.random.choice(temp_correct,1)))

            np.random.shuffle(temp)

            if not isHard:
                temp = np.append(temp, np.nan)

            random_answers.append(temp)
            questions.append(f"{questionPattern} {i}")

        p1 = pd.DataFrame(questions, columns=["question"])
        p2 = pd.DataFrame(random_answers, columns=["A", "B", "C", "D", "E"]).drop_duplicates()
        p3 = pd.concat([p1, p2], axis=1)

        all_correct_answers = []

        for index, row in p3.iterrows():
            temp_val1 = row["question"].split(" ")[-1]

            if temp_val1.isdigit() or temp_val1 in ("górna", "dolna", "środkowa", "górny", "środkowy", "dolny"):
                temp_val1 = row["question"].split(" ")[-2:]
                temp_val1 = " ".join(temp_val1)

            temp_abcde = row[["A", "B", "C", "D", "E"]].tolist()

            if isPrekambr:
                correct_answers = dataPrekambr[dataPrekambr[colName1]==temp_val1][colName2].tolist()
            else:
                correct_answers = data[data[colName1]==temp_val1][colName2].tolist()

            for answer in temp_abcde:
                if answer in correct_answers:
                    all_correct_answers.append(answer)
                    break

        p4 = pd.concat([p3, pd.DataFrame(all_correct_answers, columns=["correct_answer"])], axis=1)

        return p4  