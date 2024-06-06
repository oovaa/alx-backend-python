#!/usr/bin/env python3


"""task 6"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of floats and integers.

    Args:
        mxd_lst (List[Union[float, int]]): A list containing 
        floats and integers.

    Returns:
        float: The sum of the elements in the mixed list.

    """
    return float(sum(mxd_lst))
