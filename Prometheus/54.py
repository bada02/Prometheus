def  file_search(x,y):            
    if len(x)>1:
        for folder in x:# search in wide
            path=x[0]
            element = folder
            flag=bool
            if folder==y:
                path=path+"/"+folder
                return path
            while type (folder)==list:
                path=path+"/"+folder[0]
                for element in folder:
                    folder=element
                    if element ==y:
                        path=path+"/"+element
                        flag=True
                        return path
                    else:
                        flag=False
    else:
        flag=False
    if flag ==False:
        return False
