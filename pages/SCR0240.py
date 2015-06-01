from pages.Page import Page


class SCR0240(Page):
	"""
	SCR_0240 Amendment home
	"""
	locators = {
		"subrecipient name": xpath.text_sibling("td", "Subrecipient name", 2)
		"subrecipient principal investigator": xpath.text_sibling("td", "Subrecipient principal investigator", 2)
		"description": xpath.text_sibling("td", "Description", 2)
		"status": xpath.text_sibling("td", "Status", 2)
		"subagreement number": xpath.text_sibling("td", "Subagreement number", 2)
		"subagreement type": xpath.text_sibling("td", "Subagreement type", 2)
		"date sent to subrecipient": xpath.text_sibling("td", "Date sent to Subrecipient", 2)
		"Start date should be the new start date of the overall subagreement?": xpath.text_sibling("td", "Start date should be the new start date of the overall subagreement?", 1)
		"start date": xpath.text_sibling("td", "Start date", 2)
		"end date": xpath.text_sibling("td", "End date", 2)
		"anticipated end date": xpath.text_sibling("td", "Anticipated end date", 2)
		"subrecipient amt. to be issued": xpath.text_sibling("td", "Subrecipient amt. to be issuede", 2)
		"subrecipient anticipated": xpath.text_sibling("td", "Subrecipient anticipated", 2)
		"subrecipient indirect": xpath.text_sibling("td", "Subrecipient indirect", 2)
		"indirect basis": xpath.text_sibling("td", "Indirect basis", 2)
		"comments": xpath.text_sibling("td", "Comments", 2)
		"documents": xpath.text_sibling("td", "Documents", 2)
		"required signatures": xpath.text_sibling("td", "Required signatures", 2)
		"university authorized": "xpath=//td[contains(text(), 'Name')]/ancestor::table[1]//tr[not (@class='bg0')][position()>1]"
	
		 
			
			
			
			
			
			