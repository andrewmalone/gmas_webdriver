from pages.Page import Page
from pages.elements import Row, RText 
import utilities.xpath as xpath

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
# 		"subrecipient indirect": "xpath=//*[contains(normalize-space(text()), 'Subrecipient indirect')]/ancestor::table[1]/tbody/tr[3]/td[2]",
		"sub_IDC": "xpath=//*[contains(normalize-space(text()), 'Subrecipient indirect')]/ancestor::table[1]/tbody/tr[3]",
 		"expiration date": "xpath=//*[contains(normalize-space(text()), 'Subrecipient indirect')]/ancestor::table[1]/tbody/tr[3]/td[3]",
		"indirect basis": xpath.text_sibling("td", "Indirect basis", 1),
		"comments": "xpath=//*[contains(normalize-space(text()), 'Comments')]/../following-sibling::td[2]",
		"documents": "xpath=//*[contains(normalize-space(text()), 'Documents')]/../following-sibling::td[2]",
		"required signatures": xpath.text_sibling("td", "Required signatures", 2),
		"signature_panel": "xpath=//td[contains(text(), 'Name')]/ancestor::table[1]//tr[not (@class='bg3')][position()=2]"
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
		"sub_IDC": "css=[id='subrecipientIndirectDatatable_data']",
		"subrecipient indirect": "xpath=//tbody[@id='subrecipientIndirectDatatable_data']/tr/td",
		"expiration date": "xpath=//tbody[@id='subrecipientIndirectDatatable_data']/tr/td[2]",
		"documents": "xpath=//div[@id='documentsPanel_header']/ul/li",
		"signature_panel": "css=[id=signaturePanel_content]  tbody tr"		
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
#  	sub_indirect = RText("subrecipient indirect", "Subrecipient indirect")
# 	exp_date = RText("expiration date", "Expiration date")
	indirect_basis = RText("indirect basis", "Indirect basis")
# 	comments = RText("comments", "Comments")
	documents = RText("documents", "Documents")
# 	req_sign = RText("required signatures", "Required signatures")
	sub_IDC = RText("sub_IDC", "Sub_IDC")
	
	@classmethod
	def url(cls, subagreement_Id, segment_Id, amendment_Id):
		"""
		Direct navigation to SCR_420
		"""
		url = "{{}}/gmas/dispatch?ref=%2Fsubagreement%2FSubagreementHomeAmendmentsInclude.jsp&subagreementId={}&segmentId={}&formName=SubagreementHomeForm&amendmentId={}&ViewAmendmentEvent"
		return url.format(subagreement_Id, segment_Id, amendment_Id)
	
	@property
	def documents(self):
		"""
		Number of documents showing in the document component
		"""
		count = self.find("documents").text
		return int(count[:count.find(" ")])
	
	@property
	def sub_idc(self):
		"""
		Returns a list of sub idc rates
		//IDC_row
		"""
		return [self.IDC_row(row, self) for row in self.finds("sub_IDC") if "indirect basis" not in row.text]
  	
# 	class IDC_row(Row):
# 		locators = {
#             "rate": Row.cell(2),
#             "date": Row.cell(3)
#         }
#         _locators = {
#             "rate": Row.cell(1),
#             "date": Row.cell(2)
#         }
#    
#         rate = RText("rate")
#         date = RText("date")
  
  	
# 	def goto_documents(self):
#         """
#         Clicks the "Documents" link
#         Goes to SCR_0433
#         """
#         return self.go("documents")
        
#     def goto_comments(self):
#         """
#         Clicks the "comments" link
#         Goes to "add comments"
#         """
#         return self.go("comments")
#        
# 	def goto_subrecipient(self):
# 		"""
# 		Clicks the "Subrecipient" link
# 		Goes to scr_134b
# 		"""
# 		return self.go("subrecipient name")
# 	
# 	def goto_subrecipient_PI(self):
# 		"""
# 		Clicks the "Subrecipient" link
# 		Goes to scr_25 (Person profile)
# 		"""
# 		return self.go("subrecipient principal investigator")

	@property
	def signature_panel(self):
		"""
		List of all rows from the "Signature_panel" table
		"""
		return [self.Signature_panel(row, self) for row in self.finds("signature_panel")]
 		 
	class Signature_panel(Row):
		locators = {
			"name": Row.cell(2),
			"signature": Row.cell(6),
			"signature date": Row.cell(10)
		}	
		name = RText("name", "Name")
		signature = RText("signature", "Signature")
		signature_date = RText("signature date", "Signature date")
 
 	@property
	def signature_data(self):
		if self.mode == "old":
			return self.find("signature_panel").text.split(" ")[:10]
		if self.mode == "convert":
			return self.find("signature_panel").text.split(" ")[1][20:11]
				
			
			
			
			
			