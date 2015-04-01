import gmas_webdriver
from gmas_webdriver.pages.SCR0560 import SCR0560
from gmas_webdriver.scripts.compare_convert import wrapper


p1 = gmas_webdriver.init("Chrome", "gdev", True, position="left")
p2 = gmas_webdriver.init("Chrome", "gint", True, position="right")
p = wrapper(p1, p2)

accounts = [
    (205086, 12766),
    (10822843, 5145331),  # extra rows!
    (9613117, 5103438),
]

formats = {
    "rate_rows.date": "date",
    "rate_rows.rate": "percent",
    "history_rows.date": "date",
    "history_rows.rate": "percent",
    "history_rows.gl_date": "date"
}

for segment, account in accounts:
    p = p.goto_url(SCR0560.url(segment, account))
    print segment, account
    p.compare(formats)

p.quit()

"""
select
  '(' || ag.segment_id || ', ' || a.account_id || '),'
from
  accounts a
  join rf_account_statuses ras on a.account_status_id = ras.account_status_id
  join account_groups ag on a.account_group_id = ag.account_group_id
where
  ras.description = 'Active'
"""
