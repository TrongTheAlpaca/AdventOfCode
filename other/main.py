"""
Pretty-print Advent of Code Leaderboard in additional peform a random draw
How to use:
1. Create file 'leaderboard.json' with content from https://adventofcode.com/{year}/leaderboard/private/view/{leaderboard_id}.json
2. Edit ALL_CAPS parameters as needed.
"""

import json
import random
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, available_timezones


# Customize these parameters as needed
RANDOM_SEED = 123456
PREFERRED_TIMEZONE = "Europe/Oslo"
RANDOM_DRAW_GOLD_STAR_THRESHOLD = 5
RANDOM_DRAW_NUM_OF_MEMBERS = 6
INELIGBLE_MEMBERS_FOR_RANDOM_DRAW = []

random.seed(RANDOM_SEED)

if PREFERRED_TIMEZONE in available_timezones():
    selected_timezone = ZoneInfo(PREFERRED_TIMEZONE)
else:
    print("WARNING: Missing 'tzdata'. Run 'pip install tzdata'. Using UTC as fallback.")
    selected_timezone = timezone.utc


def draw_leaderboard(members):
    leaderboard_str = ""
    for idx, member in enumerate(members, start=1):
        leaderboard_str += f"{idx:2}: {member['name']:.<30}{member['n_stars']:>2}* ({member['n_silver_stars']:>2} silver + {member['n_gold_stars']:>2} gold) [Last Star: {member['last_star_timestamp']}]\n"
    print(leaderboard_str)


with open("leaderboard.json", "r", encoding="utf8") as f:
    leaderboard = json.load(f)


members = []
for m_idx, member in leaderboard["members"].items():

    n_gold_stars = len(
        [
            day
            for day, day_stars in member["completion_day_level"].items()
            if len(day_stars) == 2
        ]
    )

    members.append(
        {
            "id": m_idx,
            "name": (member["name"] or f"anonymous user #{m_idx}"),
            "n_stars": member["stars"],
            "n_silver_stars": member["stars"] - (n_gold_stars * 2),
            "n_gold_stars": n_gold_stars,
            "last_star_timestamp": datetime.fromtimestamp(
                member["last_star_ts"], tz=timezone.utc
            ).astimezone(selected_timezone),
        }
    )


sorted_members = sorted(
    members, key=lambda m: (-m["n_stars"], m["last_star_timestamp"])
)

print("\nTop 10 leaderboard:")
draw_leaderboard(sorted_members[0:10])

eligible_members = list(
    filter(
        lambda member: (
            RANDOM_DRAW_GOLD_STAR_THRESHOLD <= member["n_gold_stars"]
            and member["name"] not in INELIGBLE_MEMBERS_FOR_RANDOM_DRAW
            and member not in sorted_members[0:2]
        ),
        sorted_members,
    )
)

print("Random Draw:")
shuffled_leaderboard = random.sample(eligible_members, len(eligible_members))
draw_leaderboard(shuffled_leaderboard[0:RANDOM_DRAW_NUM_OF_MEMBERS])
