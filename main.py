from getlink import *
from getdata import *
from formatdata import *
from writefile import *
from userinput import*
from pathlib import Path



def main():
    user_input_value = userinput.get_user_input()
    new_user_input = getlink.get_user_input_str(user_input_value)
    new_link = getlink.get_new_link(new_user_input)

    pandas_table = getdata.convert_thumbnailurl_to_html(getdata.open_link_in_pandas(new_link))
    formatted_table = formatdata.format_pandas_table(pandas_table)
    html_table = formatdata.convert_pandas_html(formatted_table)

    current_directory = str(Path.cwd())
    viewer_file = writefile.get_viewer_file_path(current_directory)
    writefile.write_html_to_viewer(viewer_file,html_table)
            
    print('Open viewer.html to display Photo Album')
    user_input_answer = userinput.get_user_input_answer()

main()
while userinput.viewcount == userinput.yes:
    main()
    if userinput.viewcount == userinput.no:
        break

      










