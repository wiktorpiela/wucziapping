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
                             colNameScope:str, categoryTxt:str,
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
        
        category = []
        targets=[]
        correct_answers = []
        possible_answers = []

        for target in target_list:
            category.append(categoryTxt)
            targets.append(target)
            correct_array = data[data[colNameTarget]==target][colNameScope].unique()
            wrong_array = [element for element in scope_list if element not in correct_array]

            pos, corr = self.make_answers(correct_array, wrong_array, nPossibleAnswers, isMulti)
            possible_answers.append(','.join(pos))
            correct_answers.append(','.join(corr))

        df1=pd.DataFrame({
            'category': category,
            'target': targets,
            'possible_answers':possible_answers,
            'correct_answer':correct_answers
        })

        # df2=pd.DataFrame(possible_answers)
        # df2.columns = self.colNames[:len(df2.columns)]
        
        # df_final = pd.concat([df1, df2], axis=1)

        return df1
        
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
        category = []
        wrong_scopes = []
        targets_out = []

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
            category.append(questionTxt)
            targets_out.append(target)

        df_out = pd.DataFrame({
            'category': category,
            'target': targets_out,
            'scope': scopes,
            'wrong_scope': wrong_scopes,
        })

        return df_out
    
    def prepare_flashcards(self, dataSource:str, targetName:str, targetCol:str, 
                           scopeName:str, scopeCol:str, is_hard:bool):
        
        data = self.inputDataPrecambrian if dataSource=='precambrian' else self.inputDataNonPrecambrian
        scopes = data[data[scopeCol]!='brak'][scopeCol].unique()

        targets_corr = []
        targets_wrong = []
        scopes_out = []
        category = []

        for scope in scopes:
            temp_corr_target = data[(data[scopeCol]==scope) & (data[targetCol]!='brak')][targetCol].unique()[0]
            temp_wrong_target = np.nan

            if is_hard:
                temp_wrong_target = data[(data[scopeCol]!=scope) & (data[targetCol]!='brak')][targetCol].unique()
                temp_wrong_target = np.random.choice(temp_wrong_target, 5, replace=False)
                temp_wrong_target = ','.join(temp_wrong_target)

            targets_corr.append(temp_corr_target)
            targets_wrong.append(temp_wrong_target)
            scopes_out.append(scope)
            category.append(f'{targetName} {scopeName}')

        df_out = pd.DataFrame({
            'category': category,
            'scope': scopes_out,
            'target_correct': targets_corr,
            'target_wrong': targets_wrong
        })\
        .drop_duplicates()\
        .reset_index(drop=True)

        return df_out


            




        
        


