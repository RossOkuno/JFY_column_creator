def JFY_column(date, start_month):
    """
    return:Fiscal year (month, day not included)
    input:date (timestamp)
    """
    end_month_fy = start_month - 1
    if date.month <= end_month_fy:
        fy = date.year - 1
        return fy
    else:
        fy = date.year
        return fy