def calculate_bmi(height, weight):
    """
    This function responds to a request for /api/calculate_bmi/{height}&{weight}
    and returns the bmi
    :param height:   height in m
    :param weight:   weight in kg
    :return:        bmi
    """
    return weight/(height**2)