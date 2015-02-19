import time


def submit_oar_create(p, db=None):
    url = "{}/gmas/monitor/index.xhtml".format(p.env_url)
    p.driver.get(url)

    select = p.driver.find_element_by_id("indexForm:process")
    from selenium.webdriver.support.select import Select as WDSelect
    select = WDSelect(select)
    select.select_by_value("submitOneTimeJob")

    submit = p.driver.find_element_by_id("indexForm:j_idt12")
    submit.click()

    if db is None:
        from gmas_webdriver import init_db
        db = init_db(p.env)

    import gmas_webdriver.database.db as database
    status_query = """
        select
          INTERFACE_RUN_STATUS_ID
        from
          interface_batch_headers ih
        where
          ih.INTERFACE_BATCH_HEADER_ID = (select max(interface_batch_header_id) from interface_batch_headers where gmas_interface_id = 7560)
    """

    status = database.get_single_record(db, status_query)
    while status == 7406:
        # print status
        time.sleep(10)
        status = database.get_single_record(db, status_query)

    p.driver.back()

if __name__ == "__main__":
    import gmas_webdriver
    p = gmas_webdriver.init("Chrome", "gdev")
    submit_oar_create(p)
