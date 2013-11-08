from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_sub(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
        }

    #assumes you are on Segment home SCR0104b

    p = p.goto_subagreements()

    #SCR_0232
    p = p.goto_first_subagreement()
 
    #SCR_0233
    p = p.goto_documents()

    #SCR0433
    p = doc_folder(p, f)

	
    return p
