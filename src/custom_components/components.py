import pandas as pd
from haystack.core.component import component


@component
class ReviewData:

    @component.output_types(reviews=str)
    def run(self, csv_file_path: str):
        """
        run reads in an csv with fields author and comment and converts it into a dictionary.

        :param csv_file_path: path to csv file
        :return: dictionary with contents of the csv file
        """ 

        dataframe1 = pd.read_csv(csv_file_path)
        return {"reviews": dataframe1[["author","comment"]].head(10).to_dict("records")}
