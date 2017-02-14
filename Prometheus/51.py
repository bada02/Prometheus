def clean_list(list_to_clean):
    n=0
    for i in list_to_clean:
        a= list_to_clean[n]  
        q=n+1  
        for i in list_to_clean[q:]:
            if a==list_to_clean[q] and type(a)==type(list_to_clean[q]):
                list_to_clean[q]=None
            q=q+1
        n=n+1
    for i in range(len(list_to_clean)):
        try:
            list_to_clean.remove(None)
            
        except:
            break
    return list_to_clean
