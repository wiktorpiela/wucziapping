import pandas as pd
import numpy as np
import string

class QuestionBuilder:

    colNames = list(string.ascii_uppercase)

    def __init__(self, inputDataNonPrecambrian:pd.DataFrame, inputDataPrecambrian:pd.DataFrame):
        self.inputDataNonPrecambrian = inputDataNonPrecambrian
        self.inputDataPrecambrian = inputDataPrecambrian

    def prepare_closed_ended(self, isPrecambrian:bool, isMulti:bool, 
                             bothScopes:bool, multiplyIndex:int, 
                             nPossibleAnswers:int, colNameTarget:str, 
                             colNameScope:str, questionTxt:str,
                             excludeEmptyFromScope:bool=True, 
                             targetExclusionList:list=[]):

        if isPrecambrian:
            data=self.inputDataPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()
        else:
            data=self.inputDataNonPrecambrian[[colNameTarget, colNameScope]].drop_duplicates()

        n = len(data)
        target_list = data[~data[colNameTarget].isin(targetExclusionList)][colNameTarget].unique()
        target_list = [ele for ele in target_list for i in range(n*multiplyIndex)]

        if bothScopes:
            precambrianData = self.inputDataPrecambrian
            nonPrecambrianData = self.inputDataNonPrecambrian
            scope_list = np.unique(
                np.concatenate(
                    (precambrianData[colNameScope].unique(), nonPrecambrianData[colNameScope].unique())
                    )
                )
        else:        
            scope_list = data[colNameScope].unique()
            
        if excludeEmptyFromScope:
            scope_list = np.delete(scope_list, np.where(scope_list=="brak"))
        
        question_text = []
        correct_answers = []
        possible_answers = []

        for target in target_list:
            question_text.append(f"{questionTxt} {target}")
            correct_array = data[data[colNameTarget]==target][colNameScope].unique()
            wrong_array = [element for element in scope_list if element not in correct_array]

            pos, corr = self.make_answers(correct_array, wrong_array, nPossibleAnswers, isMulti)
            possible_answers.append(pos)
            correct_answers.append(corr)

        df1=pd.DataFrame({
            'question':question_text,
            'correct_answer':correct_answers
        })

        df2=pd.DataFrame(possible_answers)
        df2.columns = self.colNames[:len(df2.columns)]
        
        df_final = pd.concat([df1, df2], axis=1)

        return df_final
        
    @staticmethod
    def make_answers(correct_array:list, wrong_array:list, maxIndex:int, isMulti:bool):

        if isMulti:
            if len(correct_array)>9:
                randomSampleCorrectSize = np.random.randint(1, maxIndex+1)
            elif len(correct_array)==1:
                randomSampleCorrectSize=1
            else:
                randomSampleCorrectSize = np.random.randint(1, len(correct_array))
        else:
            randomSampleCorrectSize=1

        wrongSample = maxIndex-randomSampleCorrectSize
        temp_wrong_answers = np.random.choice(wrong_array, wrongSample, replace=False)
        temp_correct_answers = np.random.choice(correct_array, randomSampleCorrectSize, replace=False)
        temp_possible_answers = np.concatenate((temp_correct_answers, temp_wrong_answers))

        #shuffling
        iter = np.random.randint(1, 10)
        for i in range(iter):
            np.random.shuffle(temp_possible_answers)

        return temp_possible_answers, temp_correct_answers
    
    def prepare_open_ended(self, dataSource:str, isClassic:bool, colNameTarget:str, 
                           colNameScope:str, questionTxt:str):

        if dataSource == "precambrian":
            data = self.inputDataPrecambrian
        else:
            data=self.inputDataNonPrecambrian

        targets = data[(data[colNameScope]!='brak')][colNameTarget].unique()
        scopes = []
        question_text = []
        wrong_scopes = []

        for target in targets:
            scope_core = data[(data[colNameTarget]==target) & (data[colNameScope]!='brak')][colNameScope].unique()
            temp_scope = ','.join(np.flip(scope_core))
            scopes.append(temp_scope)

            if not isClassic:
                wrong_array = data[(data[colNameTarget]!=target) & (data[colNameScope]!='brak')][colNameScope].unique()
                sampleSize = np.random.randint(1, 4)
                wrong_scope = np.random.choice(wrong_array, sampleSize, replace=False)
                wrong_scope = ','.join(wrong_scope)
            else:
                wrong_scope = np.nan

            wrong_scopes.append(wrong_scope)
            question_text.append(f"{questionTxt} {target}")

        df_out = pd.DataFrame({
            'question': question_text,
            'scope': scopes,
            'wrongScope': wrong_scopes,
        })

        return df_out
        


