from gmas_webdriver.scripts.doc_folder import doc_folder

def doc_org(p, f=None):
    if f is None:
        f = {
            # SCR_0434 Add folder
            "folder_name": "Test Folder 1",
            "org_name": "hms"
        }

    #from whatever screen you are on, brings you to GMAS Home
    p = p.goto_gmashome()

    #goes to Organizations module SCR0067
    p = p.goto_organizations()

    #SCR_0067
    p.org_name = f["org_name"]
    p.search()
    p = p.goto_first_org()

    #SCR0134a
    p = p.goto_documents()

    #SCR0433
    p = doc_folder(p, f)

    p = p.goto_gmashome()
	
    return p
