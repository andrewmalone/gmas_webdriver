from db import get_list


def get_research_team_roles(db):
    query = """
        select
          r.description
        from
          gmasprod.rf_roles r
          join gmasprod.role_category_usages rcu on r.role_id = rcu.role_id
          join gmasprod.rf_role_categories rc on rcu.role_category_id = rc.role_category_id
        where
          rc.description = 'Research team roles'
          and r.description not in ('Principal Investigator', 'Mentor', 'Other')
        """
    return get_list(db, query)


def get_admin_team_roles(db):
    query = """
        select
          r.description
        from
          gmasprod.rf_roles r
          join gmasprod.role_category_usages rcu on r.role_id = rcu.role_id
          join gmasprod.rf_role_categories rc on rcu.role_category_id = rc.role_category_id
        where
          rc.description = 'Visable project admin team'
          and r.description not in ('Principal Investigator', 'Mentor', 'Cost Share Signatory', 'Fellow Investigator')
        """
    return get_list(db, query)
