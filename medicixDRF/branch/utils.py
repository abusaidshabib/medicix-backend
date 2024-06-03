import re

def modify_branch_url(value):
    return re.sub(r'\d+', '',value)

