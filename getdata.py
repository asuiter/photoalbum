import os
import pandas
from pathlib import Path


class getdata:
    webpage_link = ''
    
    @classmethod
    #Open the link using Pandas
    def open_link_in_pandas(cls,webpage_link):
        cls.webpage_link = webpage_link
        pandas_table = pandas.read_json(webpage_link)
        return pandas_table

    @classmethod
    #Create a new column converting thumbnailUrl to HTML
    def convert_thumbnailurl_to_html(cls,pandas_table):
        pandas_table['Thumbnail Image'] = pandas_table['thumbnailUrl']\
            .str.replace(
                '(.*)',
                '<img src="\\1" style="max-height:150px;"></img>'
            )
        return pandas_table







