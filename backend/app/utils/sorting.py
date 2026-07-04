from sqlalchemy import asc, desc


def apply_sort(query, model, sort: str | None):
    """
    Generic sorting utility.

    Examples:
        full_name
        -full_name
        roll_no
        -cgpa
    """

    if not sort:
        return query

    descending = sort.startswith("-")
    field = sort[1:] if descending else sort

    if hasattr(model, field):
        column = getattr(model, field)

        if descending:
            return query.order_by(desc(column))

        return query.order_by(asc(column))

    return query