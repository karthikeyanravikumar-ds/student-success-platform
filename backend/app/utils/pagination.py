from math import ceil


def paginate(query, page: int = 1, size: int = 10):
    """
    Generic pagination utility.
    Returns:
        items,
        page,
        size,
        total,
        total_pages
    """

    total = query.count()

    items = (
        query.offset((page - 1) * size)
        .limit(size)
        .all()
    )

    return {
        "items": items,
        "page": page,
        "size": size,
        "total": total,
        "total_pages": ceil(total / size) if total else 0,
    }