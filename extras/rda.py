from collections import Counter
from copy import deepcopy

import numpy as np

def get_free_residents(resident_prefs, matching):
    """ Return a list of all residents who are currently unmatched but have a
    non-empty preference list. """

    return [
        resident
        for resident in resident_prefs
        if resident_prefs[resident]
        and not any([resident in match for match in matching.values()])
    ]


def get_worst_idx(hospital, hospital_prefs, matching):
    """ Find the index of the worst resident currently assigned to `hospital`
    according to their preferences. """

    return max(
        [
            hospital_prefs[hospital].index(resident)
            for resident in hospital_prefs[hospital]
            if resident in matching[hospital]
        ]
    )


def resident_hospital(resident_prefs, hospital_prefs, capacities):
    """ Provide a stable, resident-optimal matching for the given instance of
    HR using the algorithm set out in [Gale, Shapley 1962]. """

    matching = {hospital: [] for hospital in hospital_prefs}
    free_residents = get_free_residents(resident_prefs, matching)
    while free_residents:
        resident = free_residents[0]
        hospital = resident_prefs[resident][0]
        matching[hospital].append(resident)

        if len(matching[hospital]) > capacities[hospital]:
            worst = get_worst_idx(hospital, hospital_prefs, matching)
            resident = hospital_prefs[hospital][worst]
            matching[hospital].remove(resident)

        if len(matching[hospital]) == capacities[hospital]:
            worst = get_worst_idx(hospital, hospital_prefs, matching)
            successors = hospital_prefs[hospital][worst + 1 :]

            if successors:
                for resident in successors:
                    hospital_prefs[hospital].remove(resident)
                    if hospital in resident_prefs[resident]:
                        resident_prefs[resident].remove(hospital)

            free_residents = get_free_residents(resident_prefs, matching)

    for hospital, matches in matching.items():
        sorted_matches = sorted(matches, key=hospital_prefs[hospital].index)
        matching[hospital] = sorted_matches

    return matching


def hrt_super_res(resident_prefs, hospital_prefs, capacities):
    """ Determine whether a super-stable, resident-optimal matching exists for
    the given instance of HR. If so, return the matching. """

    # ==================================
    # Needs adjusting for ties in prefs.
    # ==================================

    matching = {h: [] for h in hospital_prefs.keys()}
    fulls = {h: False for h in hospital_prefs.keys()}
    free_residents = [r for r in resident_prefs.keys()]
    while [r for r in free_residents if resident_prefs[r]]:

        r = free_residents.pop(0)
        r_prefs = resident_prefs[r]
        h_best = r_prefs[0]
        matching[h_best] += [r]

        if len(matching[h_best]) > capacities[h_best]:
            r_worst = hospital_prefs[h_best][-1]
            if r_worst in matching[h_best]:
                matching[h_best].remove(r_worst)
            resident_prefs[r_worst].remove(h_best)
            hospital_prefs[h_best].remove(r_worst)

        if len(matching[h_best]) == capacities[h_best]:
            fulls[h_best] = True
            worst_idx = np.max(
                [
                    hospital_prefs[h_best].index(resident)
                    for resident in hospital_prefs[h_best]
                    if resident in matching[h_best]
                ]
            )

            successors = hospital_prefs[h_best][worst_idx + 1 :]
            if successors:
                for resident in successors:
                    hospital_prefs[h_best].remove(resident)
                    resident_prefs[resident].remove(h_best)

    resident_match_counts = Counter([tuple(res) for res in matching.values()])
    if np.any(
        [count > 1 for count in resident_match_counts.values()]
    ) or np.any(fulls.values()):
        raise ValueError("No super-stable matching exists.")

    print("hello")

    return matching

print(1)