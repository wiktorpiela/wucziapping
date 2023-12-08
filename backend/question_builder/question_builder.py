import pandas as pd
import numpy as np

class QuestionBuilder:

    def __init__(self, inputDataNonPrecambrian:pd.DataFrame, inputDataPrecambrian:pd.DataFrame):
        self.inputDataNonPrecambrian = inputDataNonPrecambrian
        self.inputDataPrecambrian = inputDataPrecambrian

    def prepare_single(self, isPrecambrian:bool, isHard:bool, multiplyIndex:int, colNameTarget:str, colNameScope:str, questionTxt:str):

        if isPrecambrian:
            temp=self.inputDataPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()
        else:
            temp=self.inputDataNonPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()

        n = len(temp)
        target_list = temp[colNameTarget].unique()
        target_list = [ele for ele in target_list for i in range(n*multiplyIndex)]

        if isHard:
            data = self.inputDataNonPrecambrian
            data2 = self.inputDataPrecambrian
            scope_list = np.unique(
                np.concatenate(
                    (data["PIETRO"].unique(), 
                     data["ODDZIAL"].unique(), 
                     data["SYSTEM"].unique(), 
                     data["ERA"].unique(), 
                     data2["Jednostka nieformalna"].unique(),
                     data2["Eon"].unique(), 
                     data2["Era"].unique(), 
                     data2["System"].unique()
                     )
                    )
                )
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
            if len(wrong_array)<sampleSize+1:
                print('WARNING!!!!!-------------------')
                print(wrong_array)
                print(sampleSize)
                # possible_answers.append(np.repeat(np.nan, 5))
                # correct_answers.append(np.nan)
                # continue
                raise ValueError

            temp_possible_answers = np.concatenate(
                (np.random.choice(wrong_array, sampleSize, replace=False), np.random.choice(correct_array, 1))
            )
            np.random.shuffle(temp_possible_answers)

            if not isHard:
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

        return df_final

    def prepare_multi(self, isPrecambrian:bool, multiplyIndex:int, colNameTarget:str, colNameScope:str, questionTxt:str):

        if isPrecambrian:
            temp=self.inputDataPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()
        else:
            temp=self.inputDataNonPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()

        n = len(temp)
        target_list = temp[colNameTarget].unique()
        target_list = [ele for ele in target_list for i in range(n*multiplyIndex)]

        data = self.inputDataNonPrecambrian
        data2 = self.inputDataPrecambrian
        scope_list = np.unique(
            np.concatenate(
                (data["PIETRO"].unique(), 
                    data["ODDZIAL"].unique(), 
                    data["SYSTEM"].unique(), 
                    data["ERA"].unique(), 
                    data2["Jednostka nieformalna"].unique(),
                    data2["Eon"].unique(), 
                    data2["Era"].unique(), 
                    data2["System"].unique()
                    )
                )
            )
        
        question_text = []
        correct_answers = []
        possible_answers = []

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

            if len(correct_array)>5:
                randomSampleCorrectSize = np.random.randint(1, 6)
            elif len(correct_array)==1:
                randomSampleCorrectSize=1
            else:
                randomSampleCorrectSize = np.random.randint(1,len(correct_array))

            wrongSample = 5-randomSampleCorrectSize

            temp_wrong_answers = np.random.choice(wrong_array, wrongSample, replace=False)
            temp_correct_answers = np.random.choice(correct_array, randomSampleCorrectSize, replace=False)
            temp_possible_answers = np.concatenate((temp_correct_answers, temp_wrong_answers))
            np.random.shuffle(temp_possible_answers)
            possible_answers.append(temp_possible_answers)

            correct_answers.append(temp_correct_answers)

        df1=pd.DataFrame({
            'question':question_text,
            'correct_answer':correct_answers
        })

        df2=pd.DataFrame(
            possible_answers,
            columns=["A", "B", "C", "D", "E"]
        )

        df_final = pd.concat([df1, df2], axis=1)

        return df_final

