from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_app(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
        }

    #assumes you are on Segment home SCR0104b

    p = p.goto_approvals()

    #SCR_0080
    p = p.goto_first_approval()
 
    #SCR_0081
    p = p.goto_documents()

    #SCR0433
    p = doc_folder(p, f)

	
    return p
