import os
from pathlib import Path

class writefile:

    current_directory = ''
    

    @classmethod
    #Get filepath to viewer.html
    def get_viewer_file_path(cls,current_directory):
        while True:
            cls.current_directory = current_directory
            try:
                cls.current_directory.index("/")
                viewer_file_path = cls.current_directory + "/"+"viewer.html"
                return viewer_file_path
            except:
                viewer_file_path = cls.current_directory + "\\" + "viewer.html"
                return viewer_file_path
            break
        return viewer_file_path

    @classmethod
    #Write pandas table to html file
    def write_html_to_viewer(cls,viewer_file_path,html_table):
        viewerfile = open(viewer_file_path,'w')
        viewerfile.write(html_table)
        viewerfile.close()

