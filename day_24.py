import functools
import re
from typing import List, Optional

INPUT_FILE_LINES = []  # will change


class Group:
    def __init__(self, size: int, hp: int, attack_damage: int, attack_type: str, initiative: int, vulnerabilities: set, immunities: set, immune_or_infection: bool, index: int):
        self.size = size
        self.hp = hp
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.vulnerabilities = vulnerabilities
        self.immunities = immunities
        self.immune_or_infection = immune_or_infection
        self.target = None
        self.targeted_by = None
        self.index = index


def calc_damage_to(victim: Group, attack_type: str):
    if attack_type in victim.immunities:
        return 0
    if attack_type in victim.vulnerabilities:
        return 2
    return 1


def generate_groups() -> List[Group]:
    groups = []
    immune_or_infection = True  # immune first
    group_creation_index = 1
    for line in INPUT_FILE_LINES:
        if line == "" or line == "Immune System:":
            continue
        if line == "Infection:":
            immune_or_infection = False
            group_creation_index = 1
            continue
        # 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
        match = re.fullmatch(r"(\d+) units each with (\d+) hit points (\(.*?\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)", line)
        size, hp, vulns_and_imms, attack_damage, attack_type, initiative = match.groups()
        vulnerabilities = immunities = {}
        if vulns_and_imms:
            for v_or_i in vulns_and_imms[1:-2].split("; "):
                if v_or_i.startswith("immune to"):
                    immunities = set(v_or_i[len("immune to "):].split(", "))
                else:
                    vulnerabilities = set(v_or_i[len("weak to "):].split(", "))
        group = Group(int(size), int(hp), int(attack_damage), attack_type, int(initiative), vulnerabilities, immunities, immune_or_infection, group_creation_index)
        group_creation_index += 1
        groups.append(group)
    return groups


def fight(groups) -> Optional[List[Group]]:
    prev_sum = sum(g.size for g in groups)
    while any(x.immune_or_infection for x in groups) and any(not x.immune_or_infection for x in groups):
        # TARGETING #
        groups.sort(key=lambda g: (g.attack_damage * g.size, g.initiative), reverse=True)
        for group in groups:
            # print(f"# {'Immune' if group.immune_or_infection else 'Infection'} group {group.index}")
            best_other_group = None
            most_possible_damage = 0
            for other_group in groups:
                if other_group.immune_or_infection == group.immune_or_infection or other_group.targeted_by:
                    continue
                possible_damage = calc_damage_to(other_group, group.attack_type)
                if possible_damage > most_possible_damage:
                    most_possible_damage = possible_damage
                    best_other_group = other_group
            if best_other_group:
                group.target = best_other_group
                best_other_group.targeted_by = group
                # print(f"{'Immune' if group.immune_or_infection else 'Infection'} group {group.index} would deal"
                #       f" defending group {best_other_group.index} {most_possible_damage*group.size*group.attack_damage} damage")
        # ATTACKING #
        # print()
        groups.sort(key=lambda g: g.initiative, reverse=True)
        for group in groups:
            if not group.target or group.size == 0:
                continue
            damage = group.attack_damage * group.size * calc_damage_to(group.target, group.attack_type)
            units_lost = min(damage // group.target.hp, group.target.size)
            group.target.size -= units_lost
            # print(f"{'Immune' if group.immune_or_infection else 'Infection'} group {group.index} attacks"
            #       f" defending group {group.target.index}, killing {units_lost} units")
        for group in groups:
            group.target = None
            group.targeted_by = None
        groups = [group for group in groups if group.size > 0]
        # print()
        # print()
        new_sum = sum(g.size for g in groups)
        if prev_sum == new_sum:
            # print("IT ENDS WITH A TIE")
            return None
        else:
            prev_sum = new_sum
    return groups


def solve_a(input_file_lines: List[str]) -> str:
    global INPUT_FILE_LINES
    INPUT_FILE_LINES = input_file_lines
    # SETUP #
    groups = generate_groups()
    # GAME #
    groups = fight(groups)
    # COMBAT END #
    winning_army_unit_count = sum(g.size for g in groups)
    return str(winning_army_unit_count)  # 22083


@functools.lru_cache()
def calc_fight_result(boost):
    # SETUP #
    groups = generate_groups()
    for group in groups:
        if group.immune_or_infection:
            group.attack_damage += boost
    # GAME #
    groups = fight(groups)
    # COMBAT END #
    if not groups:
        return 0  # a tie
    if any(not x.immune_or_infection for x in groups):
        return -sum(g.size for g in groups)  # negative because evil
    assert any(x.immune_or_infection for x in groups)
    return sum(g.size for g in groups)  # positive because good


def solve_b(input_file_lines: List[str]) -> str:
    global INPUT_FILE_LINES
    INPUT_FILE_LINES = input_file_lines
    min_boost = 0
    max_boost = 1
    # binary search - increase
    while calc_fight_result(max_boost) <= 0:
        min_boost = max_boost
        max_boost *= 2
    # binary search - reduce
    while min_boost != max_boost:
        mid_boost = (min_boost + max_boost) // 2
        result = calc_fight_result(mid_boost)
        if result <= 0:
            min_boost = mid_boost + 1
        else:
            max_boost = mid_boost

    assert min_boost == max_boost
    final_result = calc_fight_result(min_boost)
    return str(final_result)  # 8975 (boost = 65)
