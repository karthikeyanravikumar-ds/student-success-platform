def apply_filters(
    query,
    model,
    **filters,
):
    """
    Generic filtering utility.
    """

    for field, value in filters.items():

        if value is None:
            continue

        if hasattr(model, field):
            query = query.filter(
                getattr(model, field) == value
            )

    return query