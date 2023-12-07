import pandas as pd
import numpy as np

class ClosedEndedQuestionBuilder:

    def __init__(self, inputDataNonPrecambrian:pd.DataFrame, inputDataPrecambrian:pd.DataFrame):
        self.inputDataNonPrecambrian = inputDataNonPrecambrian
        self.inputDataPrecambrian = inputDataPrecambrian

    def prepare_single(self, isPrecambrian:bool, isHard:bool, multiplyIndex:int, colNameTarget:str, colNameScope:str, questionTxt:str):

        if isPrecambrian:
            temp=self.inputDataPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()
        else:
            temp=self.inputDataNonPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()

        n = len(temp)
        target_list = temp[colNameScope].unique()
        target_list = [ele for ele in target_list for i in range(n*multiplyIndex)]

        if isHard:
            #scope_list = temp[colNameScope].unique()
            sampleSize = 4
        else:
            scope_list = temp[colNameScope].unique()
            sampleSize = 3

        question_text = []
        possible_answers = []
        correct_answers = []

        for target in target_list:
            question_text.append(f"{questionTxt} {target}")
            correct_array = temp[temp[colNameTarget]==target][colNameScope].unique()
            wrong_array = [element for element in scope_list if element not in correct_array]

            # print(f"CORRECT {correct_array}")
            # print(f"WRONG {wrong_array}")
            # if len(wrong_array)<4:
            #     print('WARNING!!!!!-------------------')
            #     possible_answers.append(np.repeat(np.nan, 5))
            #     correct_answers.append(np.nan)
            #     continue

            temp_possible_answers = np.concatenate(
                (np.random.choice(wrong_array, sampleSize, replace=False), np.random.choice(correct_array, 1))
            )
            np.random.shuffle(temp_possible_answers)
            temp_possible_answers = np.append(temp_possible_answers, np.nan)
            for correct in temp_possible_answers:
                if correct in correct_array:
                    correct_answers.append(correct)
                    continue

            possible_answers.append(temp_possible_answers)

        df1=pd.DataFrame({
            'question':question_text,
            'correct_answer':correct_answers
        })

        df2=pd.DataFrame(
            possible_answers,
            columns=["A", "B", "C", "D", "E"]
        )

        df_final = pd.concat([df1, df2], axis=1).drop_duplicates()

    def prepare_multi(self, isPrecambrian:bool, isHard:bool, multiplyIndex:int, colNameTarget:str, colNameScope:str):
        pass
