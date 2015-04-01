# import gmas_webdriver
# from gmas_webdriver.scripts.request import rgs, samples, initiate, submit
# from gmas_webdriver.scripts.notice import log_notice
# from gmas_webdriver.scripts.research_team import confirm_team


# p = gmas_webdriver.init("Chrome", "gint", splitscreen=True)
# f = samples.minimal
# f["sponsor"] = "nih"
# f["title"] = samples.add_ts("Andrew secondary GMAS-21589")
# p = rgs(p, f)
# p = initiate(p)
# p = submit(p)
# #p = log_notice(p)
# p = confirm_team(p)

class x():
    def __init__(self):
        self.n = 1

import inspect

print inspect.getmembers(x())
