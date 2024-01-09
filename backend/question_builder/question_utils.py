import pandas as pd
import numpy as np

class DataFrameToDatabaseTables:

    def __init__(self, inputDataFrame:pd.DataFrame):
        self.inputDataFrame = inputDataFrame

    def prepare_relational_tables(self, *colNames):
        data = self.inputDataFrame
        dfs_out = []
        for col in colNames:
            new_main_df, temp_rel_df = self.make_relation(data, col)
            data = new_main_df
            dfs_out.append(temp_rel_df)
        data.insert(0, 'id', np.arange(1, len(data)+1))
        return [data] + dfs_out

    @staticmethod
    def make_relation(df, colName):
        rel_df = df[colName].drop_duplicates()\
            .drop_duplicates()\
            .to_frame()\
            .reset_index()\
            .rename(columns={'index':f'{colName}_key'})
        rel_df[f'{colName}_key'] = np.arange(1, len(rel_df)+1)
        df = pd.merge(df, rel_df, how='left', on=colName).drop(columns=colName)

        return df, rel_df