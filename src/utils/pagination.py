def paginate(items: list, page: int, per_page: int):
    start = (page - 1) * per_page
    end = start + per_page
    total = len(items)
    data = {"current": page, "total": total, "items": items[start:end]}
    return data
