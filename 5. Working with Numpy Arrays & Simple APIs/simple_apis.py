# Simple APIs

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder as lgf
import pandas as pd


def main():
    nba_teams = teams.get_teams()
    dict_nba_team = one_dict(nba_teams)
    df_teams = pd.DataFrame(dict_nba_team)
    print(df_teams.head())

    # ? search
    print(df_teams[df_teams['nickname'] == 'Warriors'])

    print("\n")

    # ? find
    gamefinder = lgf.LeagueGameFinder(team_id_nullable=1610612744)
    print(gamefinder.get_data_frames())


def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


if __name__ == "__main__":
    main()
