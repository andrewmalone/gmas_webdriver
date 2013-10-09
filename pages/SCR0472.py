from pages.Page import Page
from pages.elements import Radio


# 5001 = Continuation
# 5002 = Supplement
# 5003 = Competing renewal
# 5004 = Changes to existing segment
# 5005 = Internal requests

request_type_doc = """
    Radio button for request type selection. Options are Continuation, Supplement, Competing renewal, Changes to existing segment, and Internal requests
    """
request_type_mapping = {
    "Continuation": "5001",
    "Supplement": "5002",
    "Competing renewal": "5003",
    "Changes to existing segment": "5004",
    "Internal requests": "5005"
}

class SCR0472(Page):
    """
    SCR_0472 Select request type
    """
    locators = {
        "retro": "css=input[name='isRetroactiveRequest']",
        "request type": "css=input[name='requestTypeId']",
        "ok": "name=SelectRequestTypeNextEvent"
    }

    request_type = Radio("request type", doc=request_type_doc, mapping=request_type_mapping)
    retro = Radio("retro", "retroactive radio button (true/false)")

    def ok(self):
        """
        Click the <Next> button
        Goes to:
        * SCR_0512 (continuation)
        * SCR_0089abc (supplement, competing renewal)
        * SCR_0541 (changes to existing)
        * SCR_0542 (internal)
        """
        return self.go("ok")

