from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_loc(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
        }

    #from whatever screen you are on, brings you to GMAS Home
    p = p.goto_gmashome()

    #goes to Letter of Credit module SCR_0630
    p = p.goto_loc()

    #SCR0630
    p = p.goto_documents()

    #SCR0433
    p = doc_folder(p, f)

    p = p.goto_gmashome()
	
    return p
