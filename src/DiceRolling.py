import math
import operator


def break_condition(sum_of_dices, current_sum, relate):
    if operator.eq == relate or operator.le == relate:
        return current_sum > sum_of_dices
    if operator.lt == relate:
        return current_sum >= sum_of_dices
    # TODO for all relate ; better is to create a dictionary current_operator -> break_condition_operator
    return False


def count_events_with_sum(sum_of_dices, dice_count, current_sum, relate):
    if dice_count == 0:
        return 1 if relate(current_sum, sum_of_dices) else 0
    if break_condition(sum_of_dices, current_sum, relate):
        return 0
    else:
        return sum(
            [count_events_with_sum(sum_of_dices, dice_count - 1, current_sum + dice_val, relate)
             for dice_val in range(1, 7)]
        )


def count_events_where_sum(sum_of_dices, dice_count, relate):
    return count_events_with_sum(sum_of_dices, dice_count, 0, relate)


# Probability of getting a particular sum when rolling n dices
def probability_sum(sum_of_dices=7, dice_count=2, relate=operator.eq):
    favorable_outcomes_count = count_events_where_sum(sum_of_dices, dice_count, relate)
    total_possible_outcomes = math.pow(6, dice_count)
    return "{} / {}".format(favorable_outcomes_count, total_possible_outcomes)


n_dices = 2
for sum_of_dices in range(1, 14):
    for relate in [operator.eq, operator.lt, operator.le, operator.gt, operator.ge]:
        print "Probability of rolling {} dices and getting a sum {} to {}: {}"\
            .format(n_dices, relate.__name__, sum_of_dices, probability_sum(sum_of_dices=sum_of_dices, dice_count=n_dices, relate=relate))

