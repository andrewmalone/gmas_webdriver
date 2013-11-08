from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_seg(p, f=None):
    if f is None:
        f = {
            
        }
		
    #SCR_104b
    p = p.goto_documents()
	
    #SCR_0433
    p = doc_folder(p, f)

    return p
