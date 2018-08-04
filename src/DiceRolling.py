import math


def count_events_with_sum_equal(sum_of_dices, dice_count, current_sum):
    if dice_count == 0:
        return 1 if current_sum == sum_of_dices else 0
    elif current_sum > sum_of_dices:
        return 0
    else:
        return sum(
            [count_events_with_sum_equal(sum_of_dices, dice_count - 1, current_sum + dice_val)
             for dice_val in range(1, 7)]
        )


def count_events_where_sum_is(sum_of_dices, dice_count):
    return count_events_with_sum_equal(sum_of_dices, dice_count, 0)


# Probability of getting  particular sum when rolling n dices
def probability_sum_equal(sum_of_dices=7, dice_count=2):
    favorable_outcomes_count = count_events_where_sum_is(sum_of_dices, dice_count)
    total_possible_outcomes = math.pow(6, dice_count)
    return "{} / {}".format(favorable_outcomes_count, total_possible_outcomes)


print probability_sum_equal(3, 3)
