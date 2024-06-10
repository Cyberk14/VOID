# this file will be used to see/spot the info the internet an the files the use r will have complied inform of .pdf files and images.

def eye(data: str, image=None):
    if data and image is True:
        return data, image
    
    elif image is None:
        return data
