#Get link to photo album from URL + User input


class getlink:
    user_input = 0
    url = 'https://jsonplaceholder.typicode.com/photos?albumId='
        
    @classmethod
    def get_user_input_str(cls,user_input):
        cls.user_input = str(user_input)
    
    @classmethod
    def get_new_link(cls,link):
        link = cls.url+cls.user_input
        return link







