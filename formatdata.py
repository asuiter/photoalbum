import pandas


class formatdata:


    @classmethod
    #Format pandas table by removing columns
    def format_pandas_table(cls,pandas_table):
        pandas_table = pandas_table.drop("thumbnailUrl","columns")
        pandas_table = pandas_table.drop("albumId","columns")
        pandas_table = pandas_table.drop("url","columns")
        return pandas_table
    
    @classmethod
    #Convert pandas table to HTML Code
    def convert_pandas_html(cls,pandas_table):
        pandas_table = pandas_table.to_html(escape=False)
        return pandas_table

