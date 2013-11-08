from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_req(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
        }
	
    #assumes you are already on Request home SCR0115
 
    #SCR_0115
    p = p.goto_documents()
	
    #SCR_0433
    p = doc_folder(p, f)
	
    return p
