import re


def fun(s):
    # return True if s is a valid email, else return False
    pattern = "^[a-zA-Z0-9-_]+[@][a-zA-Z0-9]+[.][a-z]{1,3}"

    valid_email = bool(re.fullmatch(pattern, s))
    if (valid_email):
        return True
    else:
        return False


"""    
    if ("@" in s and "." in s):
        a = s.split("@",1)
        #print (a)
        username = a[0]
        #print (username)
        b = a[1].split(".")
        web = b[0]
        #print (web)
        ext = b[1]
        #print (ext)
        if(username.isalnum() or "-" in username or "_" in username):
            if(web.isalnum()):
                if(len(ext) <= 3):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
"""
