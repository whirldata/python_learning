"""process_data.py

This file will gilkdsjfdksj lfds

SPHINX -> Automat

.. note::
    dsfdfd

Note -> 

"""


__author__ = "Muthu"
__email__ = "mu@whirldatascience.com"
__status__ = "Production"

# Importing system libraries
import os
import sys
import pdb
import logging

# Importing thirdparty libraries
import pandas as pd
import pandas_profiling as pp

# Importing from project
# from .constant import VAR1

class Base:
    """This is the Base class for the whole project"""
    def __init__(self):
        self._set_logger()
        self.__private()
        self.logger.info("App")

    def __private(self):
        pass

    def _set_logger(self):
        self.logger = logging.getLogger(__name__)
        self.log_level=logging.INFO   
        
        log_format = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(log_format)

        self.logger.setLevel(self.log_level)
        self.logger.addHandler(console_handler)

class CleanData(Base):
    def __init__(self):
        pass

    def print_me(self):
        print("This is clean data")


class ProcessData(Base):
    """Process data can be used to generate reports in a HTML format from the CSV file

    :param csv_path: [Required] The valid full path of the CSV file in the server
    :type csv_path: String

    :param encoding: [OPTIONAL] This is the optional param. The value could be `utf-8` or `ISO-8859-1`
    :param encoding: String
    """
    def __init__(self, csv_path, encoding="ISO-8859-1"):
        super(ProcessData, self).__init__()
        self.encoding = encoding
        self.logger.info("Started process")
        
        # Create the dataframe for the given CSV file with the provided encoding
        self.df=pd.read_csv(csv_path, encoding=encoding)
        self.logger.info("Dataframe is ready")
        
        # Setting default reports directory
        self.report_dir = "reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

        self.__validation()
    
    def __validation(self):
        """The private function to validate the parameters"""

        if self.encoding not in ['utf-8', 'ISO-8859-1']:
            raise Exception("Invalid encoding format")


        
    def print_df(self):
        self.logger.info(self.df)
    
    def generate_report(self, df=None, file_name="output.html"):
        # type: (pd, string) -> string
        """Generating the report using pandas profiler

        :param df: Pandas dataframe

        :return: Report file path
        :rtype: String

        .. note::
            Usage of the function
            
            >>> generate_report(df)
            >>> generate_report(df=<your dataframe>)

        """
        if df is None:
            df = self.df
        profile = pp.ProfileReport(df) 

        if not file_name.endswith('.html'):
            self.logger.warn(f"The file name {file_name} not ends with .html. Renaming the filename")
            file_name = f"{file_name}.html"

        report_file = os.path.join(self.report_dir, file_name)
        profile.to_file(report_file)
        return report_file
    

    def filter_by_key(self, key, value):
        pass

if __name__ == "__main__":
    data_obj = ProcessData("~/Downloads/sales_data_sample.csv")
    raw_df = data_obj.df
    data_obj.generate_report(file_name="muthu_report")

