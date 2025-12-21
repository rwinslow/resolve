import itertools


def success_probabilities(n_dice: int, wounds: int = 0) -> dict:
    results = list(itertools.product(range(1, 7), repeat=n_dice))
    results = list(set(result) for result in results)
    min_success = 4 + wounds
    success_values = set(range(min_success, 7))
    success_values_with_a_cost = set(range(min_success, 6))
    
    successes = 0
    successes_with_a_cost = 0
    for result in results:
        successes += 1 if len(success_values.intersection(result)) > 0 else 0
        successes_with_a_cost += 1 if len(success_values_with_a_cost.intersection(result)) > 0 else 0
    probability = successes / len(results)
    probability_success_with_a_cost = successes_with_a_cost / len(results)
    return {
        "n_dice": n_dice,
        "wounds": wounds,
        "min_success_value": min_success,
        "success_values": success_values,
        "success_values_with_a_cost": success_values_with_a_cost,
        "probability": probability,
        "probability_success_with_a_cost": probability_success_with_a_cost,
        "total_outcomes": len(results),
        "successful_outcomes": successes,
        "successful_outcomes_with_a_cost": successes_with_a_cost,
    }


dice_probabilities = []
for wounds in range(0, 3):
    for n_dice in range(1, 9):
        dice_probabilities.append(success_probabilities(n_dice, wounds))


for dp in dice_probabilities:
    print(
        f"Dice: {dp['n_dice']}, Wounds: {dp['wounds']}, "
        f"Prob: {dp['probability']:.4f}, "
        f"Prob (with cost): {dp['probability_success_with_a_cost']:.4f}"
    )
