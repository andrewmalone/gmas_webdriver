import random
import gmas_webdriver.utilities.dates as dateutil
"""
default_data = {
    # 328
    "funding_instrument": "Grant",
    "payment_method": "Check",
    "loc_number": "1234",
    "arra": "false",
    "equipment": "false",
    "agency": "false",
    "ia": "false",
    "snap": "false",
    "cfda": "1234",
    "prime award": "12345",
    "org": "31240"
    # 324
    # 403b
    # 359
    "awarded_dates": [  # optional
        {
            "period": 1,
            "ob_start": "ant_start",
            "ob_end": "ant_end"
        }
    ],
    # 123
    "awarded_dollars": [
        {
            "period": 1,
            "ob_direct": "100000",
            "ob_indirect": "60000",
            "ant_direct": "100000",
            "ant_indirect": "60000"
        },
        {
            "period": ">1",
            "ant_direct": "105000",
            "ant_indirect": "61000"
        }
    ],
    # 196/474
    "accounts": [
        {
            "action": "edit",
            "name": "Main 1",
            "year": "Y1",
            "budget_period": 1,
            #"start": "start",
            #"end": "end",
            # acct group
            # country
            # location
            "idc_basis": "MTDC",
            "idc_rates": [
                ("50", "1/1/08"),
                ("60", "7/31/08")
            ],
            "location": "random",
            "fund": "new",
            "activity": "new",
            "root": "44050",
            "gl": True
        }
    ],
    "allocations": "",
    "comment": "This is a first revision test"
}
"""


def revision():
    # what is the starting point?
    # segment home?
    # notice
    pass


def awarding_revision(p, data={}):
    # starting from 309

    #global default_data
    #default_data.update(data)
    #data = default_data
    p = p.revise_project()

    # 328
    # TODO: add potential of changing optional fields
    p.funding_instrument = data["funding_instrument"]
    p.payment_method = data["payment_method"]
    if data["payment_method"] == "Letter Of Credit":
        p.loc_number = data["loc_number"]
    p.arra = data["arra"]
    p.equipment = data["equipment"]
    p.agency = data["agency"]
    if p.ia is not False:
        p.ia = data["ia"]
    if p.snap is not False:
        p.snap = data["snap"]
    if p.cfda is not False:
        p.cfda = data["cfda"]
    if p.prime is not False:
        if "prime award" in data:
            p.prime = data["prime award"]
        else:
            p.prime = "1234"
    if p.foreign is not False:
        if "foreign" in data:
            p.foreign = data["foreign"]
        else:
            p.foreign = "false"
    if "org" in data:
        p.org = data["org"]
    if "pi" in data:
        p.pi = data["pi"]
    if "discipline" in data:
        p.discipline = data["discipline"]
    if "title" in data:
        p.title = data["title"]
    if "award number" in data:
        p.award_number = data["award number"]
    p = p.ok()

    # now do edit all...
    p = p.edit_all()

    # 328 award id info
    p = p.next()

    # 324 - sponsor
    # TODO: add ability to change sponsor here
    p = p.next()

    # 403b - approval
    # TODO: add ability to make changes here
    p = p.next()

    # 359 - dates
    if "awarded_dates" in data:
        for period_data in data["awarded_dates"]:
            period = p.period(period_data["period"])
            # check for anticipated first
            if "ant_start" in period_data:
                period.ant_start = period_data["ant_start"]
            if "ant_end" in period_data:
                period.ant_end = period_data["ant_end"]
            if "ob_start" in period_data:
                if period_data["ob_start"] == "ant_start":
                    period.ob_start = period.ant_start
                else:
                    period.ob_start = period_data["ob_start"]
            if "ob_end" in period_data:
                if period_data["ob_end"] == "ant_end":
                    period.ob_end = period.ant_end
                else:
                    period.ob_end = period_data["ob_end"]
    p = p.next()

    # 123 - dollars
    # TODO - add SCR_0039
    if "awarded_dollars" in data:
        # convert if set up for future periods...
        awd_periods = [period for period in data["awarded_dollars"]]
        period_count = int(p.period_count)

        for period in awd_periods:
            if type(period["period"]) is str and period["period"][0] == ">":
                # remove the placeholder period from the data
                data["awarded_dollars"].pop()
                starting_period = int(period["period"][1])
                new_periods = []
                for i in range(starting_period + 1, period_count + 1):
                    obj = {}
                    obj.update(period)
                    obj["period"] = i
                    new_periods.append(obj)
                data["awarded_dollars"] += new_periods
        for i, period_data in enumerate(data["awarded_dollars"]):
            if "ob_direct" in period_data:
                p.ob_direct = period_data["ob_direct"]
            if "ob_indirect" in period_data:
                p.ob_indirect = period_data["ob_indirect"]
            if "ant_direct" in period_data:
                p.ant_direct = period_data["ant_direct"]
            if "ant_indirect" in period_data:
                p.ant_indirect = period_data["ant_indirect"]
            if i != len(data["awarded_dollars"]) - 1:
                p = p.next_period()
    p = p.next()

    # 549 - cost share
    p = p.next()

    # 196 - accounts
    if "accounts" in data:
        for account in data["accounts"]:
            if account["action"] == "edit":
                p = p.edit_account(account["name"])
                # 474
                if "year" in account:
                    p.year = account["year"]
                if "budget_period" in account:
                    period_dates = dateutil.budget_period_dates(p.project_snapshot.start_date, p.project_snapshot.end_date)
                    p.start = period_dates[account["budget_period"] - 1][0]
                    p.end = period_dates[account["budget_period"] - 1][1]
                if "start" in account:
                    if account["start"] == "start":
                        p.start = p.project_snapshot.start_date
                    else:
                        p.start = account["start"]
                if "end" in account:
                    if account["end"] == "end":
                        p.end = p.project_snapshot.end_date
                    else:
                        p.end = account["end"]
                if "idc_basis" in account:
                    p.idc_basis = account["idc_basis"]
                if "idc_rates" in account:
                    p = p.edit_rates()
                    for rate in account["idc_rates"]:
                        # 190
                        p.add_rate()
                        p.rate = rate[0]
                        p.date = rate[1]
                    p = p.ok()
                if "location" in account:
                    p = p.edit_location()
                    if account["location"] == "random":
                        p.location = random.choice(p.location.options)
                    else:
                        p.location = account["location"]
                    p = p.ok()
                # set the org if changing in this revision
                if "org" in data:
                    p.org = data["org"]
                if "fund" in account:
                    if account["fund"] == "new":
                        p = p.create_fund()
                        if p.fund == "" and p.fund_type is not False:
                            p.fund_type = random.choice(p.fund_type.options)
                        if p.fund == "":
                            p = p.get_new_fund()
                            # what to do if the fund still doesn't come back?
                        p = p.ok()
                if "activity" in account:
                    if account["activity"] == "new":
                        p = p.select_activity()
                        p = p.create()
                        p.a21 = random.choice(p.a21.options)
                        if p.activity == "":
                            p = p.get_activity()
                        p = p.ok()
                        p.activity = 1
                        p = p.ok()
                if "root" in account:
                    p.root = account["root"]
                p = p.ok()
                # check to send to GL?
                if "gl" in account and account["gl"] is True:
                    p.account(1).checkbox = True
                p = p.next()
    # ALLOCATIONS!!!
    if "allocations" in data:
        # for now, put all the money in the main
        p.allocation = p.remaining
        p = p.ok()

    # back on 105
    if "comment" in data:
        p.comment = data["comment"]

    p = p.commit_changes()
    p.check_all = False
    p = p.ok()
    return p


if __name__ == '__main__':
    pass
