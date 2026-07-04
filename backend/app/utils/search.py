from sqlalchemy import or_


def apply_search(
    query,
    model,
    search: str | None,
    fields: list[str],
):
    """
    Generic search utility.
    """

    if not search:
        return query

    filters = []

    for field in fields:
        if hasattr(model, field):
            filters.append(
                getattr(model, field).ilike(f"%{search}%")
            )

    return query.filter(or_(*filters))