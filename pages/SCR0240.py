from pages.Page import Page
from pages.elements import Row, RText 
import utilities.xpath as xpath
from lxml.html._diffcommand import description
from telnetlib import STATUS


class SCR0240(Page):
	"""
	SCR_0240 Amendment home
	"""
	locators = {
		"subrecipient name": xpath.text_sibling("td", "Subrecipient name", 2),
		"subrecipient principal investigator": xpath.text_sibling("td", "Subrecipient principal investigator", 2),
		"description": xpath.text_sibling("td", "Description", 2),
		"status": xpath.text_sibling("td", "Status", 2),
# 		"subagreement number": xpath.text_sibling("td", "Subagreement number", 2),
		"subagreement type": xpath.text_sibling("td", "Subagreement type", 2),
		"date sent to subrecipient": "xpath=//span[contains(normalize-space(text()), 'Date sent to Subrecipient')]/../following-sibling::td[2]",
 		"Start date should be the new start date of the overall subagreement?": xpath.text_sibling("td", "Start date should be the new start date of the overall subagreement?", 1),
		"start date": "xpath=//span[contains(normalize-space(text()), 'Start date')]/../following-sibling::td[2]",
		"end date": "xpath=//span[contains(normalize-space(text()), 'End date')]/../following-sibling::td[2]",
		"anticipated end date": "xpath=//span[contains(normalize-space(text()), 'Anticipated end date')]/../following-sibling::td[2]",
		"subrecipient amt. to be issued": "xpath=//span[contains(normalize-space(text()), 'Subrecipient amt. to be issued')]/../following-sibling::td[2]",
		"subrecipient anticipated": "xpath=//span[contains(normalize-space(text()), 'Subrecipient anticipated')]/../following-sibling::td[2]",
		"subrecipient indirect": "xpath=//*[contains(normalize-space(text()), 'Subrecipient indirect')]/ancestor::table[1]/tbody/tr[3]/td[2]",
		"expiration date": "xpath=//*[contains(normalize-space(text()), 'Subrecipient indirect')]/ancestor::table[1]/tbody/tr[3]/td[3]",
		"indirect basis": xpath.text_sibling("td", "Indirect basis", 1),
		"comments": "xpath=//*[contains(normalize-space(text()), 'Comments')]/../following-sibling::td[2]",
		"documents": "xpath=//*[contains(normalize-space(text()), 'Documents')]/../following-sibling::td[2]",
		"required signatures": xpath.text_sibling("td", "Required signatures", 2),
# 		"university authorized": "xpath=//td[contains(text(), 'Name')]/ancestor::table[1]//tr[not (@class='bg3')][position()>1]"
	}
	
	_locators = {
		"subrecipient name"	: "css=[id=summarySubrecipientLink]",
		"status": "css=[id=summaryStatusValue]",
		"subrecipient principal investigator": "css=[id=summaryPrincipleInvestigatorLink]",
		"description": "css=[id=summaryDescriptionValue]",
		"subagreement type": "css=[id=summarySubagreementTypeValue]",
		"date sent to subrecipient": "css=[id=summaryDateSenValue]",
		"start date": "xpath=//span[@id='detailsStartDateLabel']/../following-sibling::td[1]",
		"end date": "xpath=//span[contains(normalize-space(text()), 'End date')]/../following-sibling::td[1]",
		"anticipated end date": "xpath=//span[contains(normalize-space(text()), 'Anticipated end date')]/../following-sibling::td[1]",
		"subrecipient amt. to be issued": "xpath=//span[contains(normalize-space(text()), 'Subrecipient amt. to be issued')]/../following-sibling::td[1]",
		"subrecipient anticipated": "xpath=//span[contains(normalize-space(text()), 'Subrecipient anticipated')]/../following-sibling::td[1]",
		"indirect basis": "xpath=//span[contains(normalize-space(text()), 'Subrecipient indirect')]/../following-sibling::td[1]",
		"subrecipient indirect": "xpath=//tbody[@id='subrecipientIndirectDatatable_data']/tr/td",
		"expiration date": "xpath=//tbody[@id='subrecipientIndirectDatatable_data']/tr/td[2]",
		"documents": "xpath=//div[@id='j_idt189_header']/ul/li"		
	}
	
	subrecipient_name = RText("subrecipient name", "Subrecipient name")
	subrecipient_pi = RText("subrecipient principal investigator", "Subrecipient principal investigator")
	description = RText("description", "Description")
	status = RText("status", "Status")
# 	subagreement_number = RText("subagreement number", "Subagreement number")
	subagreement_type = RText("subagreement type", "Subagreement type")
	date_sent = RText("date sent to subrecipient", "Date sent to subrecipient")
# 	new_date = RText("Start date should be the new start date of the overall subagreement?", "Start date should be the new start date of the overall subagreement?")
	start_date = RText("start date", "Start date")
	end_date = RText("end date", "End date")
	anticipated_enddate = RText("anticipated end date", "Anticipated end date")
# 	subrecipient_amt = RText("subrecipient amt. to be issued", "Subrecipient amt. to be issued")
	sub_anticipated = RText("subrecipient anticipated", "Subrecipient anticipated")
	sub_indirect = RText("subrecipient indirect", "Subrecipient indirect")
	exp_date = RText("expiration date", "Expiration date")
	indirect_basis = RText("indirect basis", "Indirect basis")
# 	comments = RText("comments", "Comments")
	documents = RText("documents", "Documents")
# 	req_sign = RText("required signatures", "Required signatures")
	
	@classmethod
	def url(cls, subagreement_Id, segment_Id, amendment_Id):
		"""
		Direct navigation to SCR_420
		"""
		url = "{{}}/gmas/dispatch?ref=%2Fsubagreement%2FSubagreementHomeAmendmentsInclude.jsp&subagreementId={}&segmentId={}&formName=SubagreementHomeForm&amendmentId={}&ViewAmendmentEvent"
		return url.format(subagreement_Id, segment_Id, amendment_Id)
	
	
# 	@property
# 	def documents(self):
# 		if self.mode == "old":
# 			return self.find("documents").text.split("")[0]
# 		if self.mode == "convert":
# 			return self.find("documents").text.split(" ")[0]
	
# 	def goto_documents(self):
#         """
#         Clicks the "Documents" link
#         Goes to SCR_0433
#         """
#         return self.go("documents")
#        
#     def goto_comments(self):
#         """
#         Clicks the "comments" link
#         Goes to "add comments"
#         """
#         return self.go("comments")

# 	@property
# 	def university_authorized(self):
# 		"""
# 		List of all rows from the "University_authorized" table
# 		"""
# 		return [self.University_authorized(row, self) for row in self.finds("university authorized")]
# 		 
# 	class University_authorized(Row):
# 		locators = {
# 		"name": Row.cell(2),
# 		"signature": Row.cell(6),
# 		"signature date": Row.cell(10)
# 		}	
# 		name = RText("name", "Name"),
# 		signature = RText("signature", "Signature"),
# 		signature_date = RText("signature date", "Signature date")
		
			
			
			
			
			