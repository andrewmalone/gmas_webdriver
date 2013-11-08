def doc_folder(p, f=None):
    if f is None:
        f = {

        }

    #SCR_0433
    p = p.add_folder()
	
    #SCR_0434
    p.folder_name = f["folder_name"]
    p = p.ok()
	
    #SCR_0433
    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc1.pdf")
    p.description = ("Testing File Upload 1 Readonly")
    p.readonly = True
    p = p.ok()
	
    #SCR_0433
    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc2.pdf")
    p.description = ("Testing File Upload 2 CheckIn - Not Read Only")
    p.readonly = False
    p = p.ok()

    #SCR_0433
    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc3.pdf")
    p.description = ("No Description")
    p.readonly = False
    p = p.ok()

    #SCR_0433  
    #p.document(2).check()
    #p = p.lock()

    #Delete third document in list
    #SCR_0433
    p = p.document("001TestDoc3.pdf").go()

    #SCR_0135
    p = p.delete()

    #SCR_0136
    p = p.ok()

    # Rename and edit description of first document in list
    #SCR_0433
    p = p.document(1).go()

    #SCR_0135
    p = p.rename()

    #SCR_0137
    p.new_name = f["new_name"]
    p = p.ok()

    #SCR_0135
    p = p.edit_desc()

    #SCR_0141a
    p.description = ("Editing Description")
    p = p.ok()

    #SCR_0135
    p = p.last_breadcrumb().last_breadcrumb()

    #Lock and unlock a doc
    #SCR_0433
    i = 1
    while (p.document(i).status != 'Checked in'):
        i += 1

    p.document(i).check()
    p.lock()
    p = p.document(i).go()

    #SCR_0135
    p.unlock()

    p = p.last_breadcrumb()

    #Checkout, Unlock and Checkin second document
    #While look to get checked in docs only
    #SCR_0433
    """i = 1
    while (p.document(i).status != 'Checked in'):
        i += 1

    p = p.document(i).go()
    
    #SCR_0135
    p.checkout()
    p.unlock()
    p.checkout()
    p = p.checkin()

    #SCR_0138
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc4.pdf")
    p.description = ("Checked in after checkout")
    p = p.ok()

    #p = p.last_breadcrumb()"""

    #Get doc from clipboard
    #SCR_0433
    p = p.get_doc()

    #SCR_0138
    p.document(1).check()
    p = p.ok()
    """
    #Get email from clipboard
    #SCR_0433
    p = p.get_doc()

    #SCR_0138
    i = 1
    while (p.document(i).type != 'Email'):
        i += 1

    p.document(i).check()
    p = p.ok()
    """
    #Moves doc to clipboard
    #SCR_0433
    i = 1
    while (p.document(i).status != 'Checked in'):
        i += 1

    p.document(i).check()
    p = p.move_doc()

    #SCR_0139
    p = p.last_breadcrumb()
    """
    #Delete email
    #SCR_0433
    i = 1
    while (p.document(i).type != 'Email'):
        i += 1

    p.document(i).check()
    p.delete()

    #SCR_0136
    p = p.ok()
    """
    #work inside the new folder created
    #SCR_0433
    p = p.folder(1).go()
    #now still on SCR_0433 but inside the subfolder

    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc4.pdf")
    p.description = ("Testing File Upload 4 Readonly inside a subfolder")
    p.readonly = True
    p = p.ok()
    
    #SCR_0433
    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc5.pdf")
    p.description = ("Testing File Upload 5 CheckIn - Not Read Only inside a subfolder")
    p.readonly = False
    p = p.ok()

    #SCR_0433
    p = p.add_document()
                        
    #SCR_0141a
    p.filename = ("C:\\\\Python27\\\\TestDocsToUpload\\\\001TestDoc6.pdf")
    p.description = ("No Description inside a subfolder")
    p.readonly = False
    p = p.ok()

    p = p.last_breadcrumb()

    return p
