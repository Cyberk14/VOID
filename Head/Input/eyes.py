# this file will be used to see/spot the info the internet and the files the user  will have complied inform of .pdf files and images.

def see(data: str, image=None):
    if data and image is True:
        return data, image
    
    elif image is None:
        return data
