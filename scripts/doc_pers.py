from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_pers(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
        }

    #from whatever screen you are on, brings you to Person screen
    p = p.global_header.goto_person_link()

    #SCR0025
    p = p.goto_documents()

    #SCR0433
    p = doc_folder(p, f)

    p = p.goto_gmashome()
	
    return p
