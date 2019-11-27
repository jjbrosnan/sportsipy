PARSING_SCHEME = {
    'name': 'a',
    'conference': 'td[data-stat="conf_abbr"] a',
    'games': 'td[data-stat="g"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'win_percentage': 'td[data-stat="win_loss_pct"]:first',
    'conference_wins': 'td[data-stat="wins_conf"]:first',
    'conference_losses': 'td[data-stat="losses_conf"]:first',
    'conference_win_percentage': 'td[data-stat="win_loss_pct_conf"]:first',
    'points_per_game': 'td[data-stat="points_per_g"]:first',
    'points_against_per_game': 'td[data-stat="opp_points_per_g"]:first',
    'simple_rating_system': 'td[data-stat="srs"]:first',
    'strength_of_schedule': 'td[data-stat="sos"]:first',
    'current_rank': 'td[data-stat="rank_current"]:first',
    'preseason_rank': 'td[data-stat="rank_pre"]:first',
    'highest_rank': 'td[data-stat="rank_min"]:first',
    'pass_completions': 'td[data-stat="pass_cmp"]:first',
    'opponents_pass_completions': 'td[data-stat="opp_pass_cmp"]:first',
    'pass_attempts': 'td[data-stat="pass_att"]:first',
    'opponents_pass_attempts': 'td[data-stat="opp_pass_att"]:first',
    'pass_completion_percentage': 'td[data-stat="pass_cmp_pct"]:first',
    'opponents_pass_completion_percentage':
        'td[data-stat="opp_pass_cmp_pct"]:first',
    'pass_yards': 'td[data-stat="pass_yds"]:first',
    'opponents_pass_yards': 'td[data-stat="opp_pass_yds"]:first',
    'interceptions': 'td[data-stat="pass_int"]:first',
    'opponents_interceptions': 'td[data-stat="opp_pass_int"]:first',
    'pass_touchdowns': 'td[data-stat="pass_td"]:first',
    'opponents_pass_touchdowns': 'td[data-stat="opp_pass_td"]:first',
    'rush_attempts': 'td[data-stat="rush_att"]:first',
    'opponents_rush_attempts': 'td[data-stat="opp_rush_att"]:first',
    'rush_yards': 'td[data-stat="rush_yds"]:first',
    'opponents_rush_yards': 'td[data-stat="opp_rush_yds"]:first',
    'rush_yards_per_attempt': 'td[data-stat="rush_yds_per_att"]:first',
    'opponents_rush_yards_per_attempt':
        'td[data-stat="opp_rush_yds_per_att"]:first',
    'rush_touchdowns': 'td[data-stat="rush_td"]:first',
    'opponents_rush_touchdowns': 'td[data-stat="opp_rush_td"]:first',
    'plays': 'td[data-stat="tot_plays"]:first',
    'opponents_plays': 'td[data-stat="opp_tot_plays"]:first',
    'yards': 'td[data-stat="tot_yds"]:first',
    'opponents_yards': 'td[data-stat="opp_tot_yds"]:first',
    'turnovers': 'td[data-stat="turnovers"]:first',
    'opponents_turnovers': 'td[data-stat="opp_turnovers"]:first',
    'fumbles_lost': 'td[data-stat="fumbles_lost"]:first',
    'opponents_fumbles_lost': 'td[data-stat="opp_fumbles_lost"]:first',
    'yards_per_play': 'td[data-stat="tot_yds_per_play"]:first',
    'opponents_yards_per_play': 'td[data-stat="opp_tot_yds_per_play"]:first',
    'pass_first_downs': 'td[data-stat="first_down_pass"]:first',
    'opponents_pass_first_downs': 'td[data-stat="opp_first_down_pass"]:first',
    'rush_first_downs': 'td[data-stat="first_down_rush"]:first',
    'opponents_rush_first_downs': 'td[data-stat="opp_first_down_rush"]:first',
    'first_downs_from_penalties': 'td[data-stat="first_down_penalty"]:first',
    'opponents_first_downs_from_penalties':
        'td[data-stat="opp_first_down_penalty"]:first',
    'first_downs': 'td[data-stat="first_down"]:first',
    'opponents_first_downs': 'td[data-stat="opp_first_down"]:first',
    'penalties': 'td[data-stat="penalty"]:first',
    'opponents_penalties': 'td[data-stat="opp_penalty"]:first',
    'yards_from_penalties': 'td[data-stat="penalty_yds"]:first',
    'opponents_yards_from_penalties': 'td[data-stat="opp_penalty_yds"]:first'
}

SCHEDULE_SCHEME = {
    'game': 'th[data-stat="g"]:first',
    'date': 'td[data-stat="date_game"]:first',
    'time': 'td[data-stat="time_game"]:first',
    'day_of_week': 'td[data-stat="day_name"]:first',
    'location': 'td[data-stat="game_location"]:first',
    'rank': 'td[data-stat="school_name"]:first',
    'opponent_rank': 'td[data-stat="opp_name"]:first',
    'opponent_name': 'td[data-stat="opp_name"]:first',
    'opponent_abbr': 'td[data-stat="opp_name"]:first',
    'opponent_conference': 'td[data-stat="conf_abbr"]:first',
    'result': 'td[data-stat="game_result"]:first',
    'points_for': 'td[data-stat="points"]:first',
    'points_against': 'td[data-stat="opp_points"]:first',
    'wins': 'td[data-stat="wins"]:first',
    'losses': 'td[data-stat="losses"]:first',
    'streak': 'td[data-stat="game_streak"]:first'
}

BOXSCORE_SCHEME = {
    'date': 'div[class="scorebox_meta"]:first',
    'time': 'div[class="scorebox_meta"]:first',
    'stadium': 'div[class="scorebox_meta"]:first',
    'attendance': 'div[class="scorebox_meta"]:first',
    'duration': 'div[class="scorebox_meta"]:first',
    'home_name': 'a[itemprop="name"]:first',
    'away_name': 'a[itemprop="name"]:last',
    'away_points': 'div[class="scorebox"] div[class="score"]',
    'away_first_downs': 'td[data-stat="vis_stat"]',
    'away_rush_attempts': 'td[data-stat="vis_stat"]',
    'away_rush_yards': 'td[data-stat="vis_stat"]',
    'away_rush_touchdowns': 'td[data-stat="vis_stat"]',
    'away_pass_completions': 'td[data-stat="vis_stat"]',
    'away_pass_attempts': 'td[data-stat="vis_stat"]',
    'away_pass_yards': 'td[data-stat="vis_stat"]',
    'away_pass_touchdowns': 'td[data-stat="vis_stat"]',
    'away_interceptions': 'td[data-stat="vis_stat"]',
    'away_times_sacked': 'td[data-stat="vis_stat"]',
    'away_yards_lost_from_sacks': 'td[data-stat="vis_stat"]',
    'away_net_pass_yards': 'td[data-stat="vis_stat"]',
    'away_total_yards': 'td[data-stat="vis_stat"]',
    'away_fumbles': 'td[data-stat="vis_stat"]',
    'away_fumbles_lost': 'td[data-stat="vis_stat"]',
    'away_turnovers': 'td[data-stat="vis_stat"]',
    'away_penalties': 'td[data-stat="vis_stat"]',
    'away_yards_from_penalties': 'td[data-stat="vis_stat"]',
    'away_third_down_conversions': 'td[data-stat="vis_stat"]',
    'away_third_down_attempts': 'td[data-stat="vis_stat"]',
    'away_fourth_down_conversions': 'td[data-stat="vis_stat"]',
    'away_fourth_down_attempts': 'td[data-stat="vis_stat"]',
    'away_time_of_possession': 'td[data-stat="vis_stat"]',
    'home_points': 'div[class="scorebox"] div[class="score"]',
    'home_first_downs': 'td[data-stat="home_stat"]',
    'home_rush_attempts': 'td[data-stat="home_stat"]',
    'home_rush_yards': 'td[data-stat="home_stat"]',
    'home_rush_touchdowns': 'td[data-stat="home_stat"]',
    'home_pass_completions': 'td[data-stat="home_stat"]',
    'home_pass_attempts': 'td[data-stat="home_stat"]',
    'home_pass_yards': 'td[data-stat="home_stat"]',
    'home_pass_touchdowns': 'td[data-stat="home_stat"]',
    'home_interceptions': 'td[data-stat="home_stat"]',
    'home_times_sacked': 'td[data-stat="home_stat"]',
    'home_yards_lost_from_sacks': 'td[data-stat="home_stat"]',
    'home_net_pass_yards': 'td[data-stat="home_stat"]',
    'home_total_yards': 'td[data-stat="home_stat"]',
    'home_fumbles': 'td[data-stat="home_stat"]',
    'home_fumbles_lost': 'td[data-stat="home_stat"]',
    'home_turnovers': 'td[data-stat="home_stat"]',
    'home_penalties': 'td[data-stat="home_stat"]',
    'home_yards_from_penalties': 'td[data-stat="home_stat"]',
    'home_third_down_conversions': 'td[data-stat="home_stat"]',
    'home_third_down_attempts': 'td[data-stat="home_stat"]',
    'home_fourth_down_conversions': 'td[data-stat="home_stat"]',
    'home_fourth_down_attempts': 'td[data-stat="home_stat"]',
    'home_time_of_possession': 'td[data-stat="home_stat"]'
}

BOXSCORE_SCHEME = {
    'date': 'div[class="scorebox_meta"]:first',
    'time': 'div[class="scorebox_meta"]:first',
    'stadium': 'div[class="scorebox_meta"]:first',
    'summary': 'table[class="linescore nohover stats_table no_freeze"]:first',
    'home_name': 'a[itemprop="name"]:last',
    'away_name': 'a[itemprop="name"]:first',
    'away_points': 'div[class="scorebox"] div[class="score"]',
    'away_first_downs': 'td[data-stat="vis_stat"]',
    'away_rush_attempts': 'td[data-stat="vis_stat"]',
    'away_rush_yards': 'td[data-stat="vis_stat"]',
    'away_rush_touchdowns': 'td[data-stat="vis_stat"]',
    'away_pass_completions': 'td[data-stat="vis_stat"]',
    'away_pass_attempts': 'td[data-stat="vis_stat"]',
    'away_pass_yards': 'td[data-stat="vis_stat"]',
    'away_pass_touchdowns': 'td[data-stat="vis_stat"]',
    'away_interceptions': 'td[data-stat="vis_stat"]',
    'away_total_yards': 'td[data-stat="vis_stat"]',
    'away_fumbles': 'td[data-stat="vis_stat"]',
    'away_fumbles_lost': 'td[data-stat="vis_stat"]',
    'away_turnovers': 'td[data-stat="vis_stat"]',
    'away_penalties': 'td[data-stat="vis_stat"]',
    'away_yards_from_penalties': 'td[data-stat="vis_stat"]',
    'home_points': 'div[class="scorebox"] div[class="score"]',
    'home_first_downs': 'td[data-stat="home_stat"]',
    'home_rush_attempts': 'td[data-stat="home_stat"]',
    'home_rush_yards': 'td[data-stat="home_stat"]',
    'home_rush_touchdowns': 'td[data-stat="home_stat"]',
    'home_pass_completions': 'td[data-stat="home_stat"]',
    'home_pass_attempts': 'td[data-stat="home_stat"]',
    'home_pass_yards': 'td[data-stat="home_stat"]',
    'home_pass_touchdowns': 'td[data-stat="home_stat"]',
    'home_interceptions': 'td[data-stat="home_stat"]',
    'home_total_yards': 'td[data-stat="home_stat"]',
    'home_fumbles': 'td[data-stat="home_stat"]',
    'home_fumbles_lost': 'td[data-stat="home_stat"]',
    'home_turnovers': 'td[data-stat="home_stat"]',
    'home_penalties': 'td[data-stat="home_stat"]',
    'home_yards_from_penalties': 'td[data-stat="home_stat"]',
}

BOXSCORE_ELEMENT_INDEX = {
    'date': 0,
    'time': 1,
    'stadium': 2,
    'away_points': 0,
    'away_first_downs': 0,
    'away_rush_attempts': 1,
    'away_rush_yards': 1,
    'away_rush_touchdowns': 1,
    'away_pass_completions': 2,
    'away_pass_attempts': 2,
    'away_pass_yards': 2,
    'away_pass_touchdowns': 2,
    'away_interceptions': 2,
    'away_total_yards': 3,
    'away_fumbles': 4,
    'away_fumbles_lost': 4,
    'away_turnovers': 5,
    'away_penalties': 6,
    'away_yards_from_penalties': 6,
    'home_points': 1,
    'home_first_downs': 0,
    'home_rush_attempts': 1,
    'home_rush_yards': 1,
    'home_rush_touchdowns': 1,
    'home_pass_completions': 2,
    'home_pass_attempts': 2,
    'home_pass_yards': 2,
    'home_pass_touchdowns': 2,
    'home_interceptions': 2,
    'home_total_yards': 3,
    'home_fumbles': 4,
    'home_fumbles_lost': 4,
    'home_turnovers': 5,
    'home_penalties': 6,
    'home_yards_from_penalties': 6
}

# Designates the index of the item within the requested tag
BOXSCORE_ELEMENT_SUB_INDEX = {
    'away_rush_attempts': 0,
    'away_rush_yards': 1,
    'away_rush_touchdowns': 2,
    'away_pass_completions': 0,
    'away_pass_attempts': 1,
    'away_pass_yards': 2,
    'away_pass_touchdowns': 3,
    'away_interceptions': 4,
    'away_fumbles': 0,
    'away_fumbles_lost': 1,
    'away_penalties': 0,
    'away_yards_from_penalties': 1,
    'home_rush_attempts': 0,
    'home_rush_yards': 1,
    'home_rush_touchdowns': 2,
    'home_pass_completions': 0,
    'home_pass_attempts': 1,
    'home_pass_yards': 2,
    'home_pass_touchdowns': 3,
    'home_interceptions': 4,
    'home_fumbles': 0,
    'home_fumbles_lost': 1,
    'home_penalties': 0,
    'home_yards_from_penalties': 1
}

PLAYER_SCHEME = {
    'season': 'th[data-stat="year_id"]',
    'name': 'h1[itemprop="name"]',
    'team_abbreviation': 'td[data-stat="school_name"]',
    'position': 'td[data-stat="pos"]',
    'height': 'span[itemprop="height"]',
    'weight': 'span[itemprop="weight"]',
    'year': 'td[data-stat="class"]',
    'games': 'td[data-stat="g"]',
    'completed_passes': 'td[data-stat="pass_cmp"]',
    'pass_attempts': 'td[data-stat="pass_att"]',
    'passing_completion': 'td[data-stat="pass_cmp_pct"]',
    'passing_touchdowns': 'td[data-stat="pass_td"]',
    'interceptions_thrown': 'td[data-stat="pass_int"]',
    'passing_yards_per_attempt': 'td[data-stat="pass_yds_per_att"]',
    'adjusted_yards_per_attempt': 'td[data-stat="adj_pass_yds_per_att"]',
    'quarterback_rating': 'td[data-stat="pass_rating"]',
    'rush_attempts': 'td[data-stat="rush_att"]',
    'rush_yards': 'td[data-stat="rush_yds"]',
    'rush_yards_per_attempt': 'td[data-stat="rush_yds_per_att"]',
    'rush_touchdowns': 'td[data-stat="rush_td"]',
    'receptions': 'td[data-stat="rec"]',
    'receiving_yards': 'td[data-stat="rec_yds"]',
    'receiving_yards_per_reception': 'td[data-stat="rec_yds_per_rec"]',
    'receiving_touchdowns': 'td[data-stat="rec_td"]',
    'plays_from_scrimmage': 'td[data-stat="scrim_att"]',
    'yards_from_scrimmage': 'td[data-stat="scrim_yds"]',
    'yards_from_scrimmage_per_play': 'td[data-stat="scrim_yds_per_att"]',
    'rushing_and_receiving_touchdowns': 'td[data-stat="scrim_td"]',
    'solo_tackles': 'td[data-stat="tackles_solo"]',
    'assists_on_tackles': 'td[data-stat="tackles_assists"]',
    'total_tackles': 'td[data-stat="tackles_total"]',
    'tackles_for_loss': 'td[data-stat="tackles_loss"]',
    'sacks': 'td[data-stat="sacks"]',
    'interceptions': 'td[data-stat="def_int"]',
    'yards_returned_from_interceptions': 'td[data-stat="def_int_yds"]',
    'yards_returned_per_interception': 'td[data-stat="def_int_yds_per_int"]',
    'interceptions_returned_for_touchdown': 'td[data-stat="def_int_td"]',
    'passes_defended': 'td[data-stat="pass_defended"]',
    'fumbles_recovered': 'td[data-stat="fumbles_rec"]',
    'yards_recovered_from_fumble': 'td[data-stat="fumbles_rec_yds"]',
    'fumbles_recovered_for_touchdown': 'td[data-stat="fumbles_rec_td"]',
    'fumbles_forced': 'td[data-stat="fumbles_forced"]',
    'punt_return_touchdowns': 'td[data-stat="td_punt_ret"]',
    'kickoff_return_touchdowns': 'td[data-stat="td_kick_ret"]',
    'other_touchdowns': 'td[data-stat="td_other"]',
    'total_touchdowns': 'td[data-stat="td_total"]',
    'extra_points_made': 'td[data-stat="xpm"]',
    'field_goals_made': 'td[data-stat="fgm"]',
    'two_point_conversions': 'td[data-stat="two_pt_md"]',
    'safeties': 'td[data-stat="safety_md"]',
    'points': 'td[data-stat="points"]',
    'passing_yards': 'td[data-stat="pass_yds"]',
    'pass_yards_per_attempt': 'td[data-stat="pass_yds_per_att"]',
    'kickoff_returns': 'td[data-stat="kick_ret"]',
    'kickoff_return_yards': 'td[data-stat="kick_ret_yds"]',
    'average_kickoff_return_yards': 'td[data-stat="kick_ret_yds_per_ret"]',
    'punt_returns': 'td[data-stat="punt_ret"]',
    'punt_return_yards': 'td[data-stat="punt_ret_yds"]',
    'average_punt_return_yards': 'td[data-stat="punt_ret_yds"]',
    'extra_points_attempted': 'td[data-stat="xpa"]',
    'extra_point_percentage': 'td[data-stat="xp_pct"]',
    'field_goals_attempted': 'td[data-stat="fga"]',
    'field_goal_percentage': 'td[data-stat="fg_pct"]',
    'points_kicking': 'td[data-stat="kick_points"]',
    'punts': 'td[data-stat="punt"]',
    'punting_yards': 'td[data-stat="punt_yds"]',
    'punting_yards_per_attempt': 'td[data-stat="punt_yds_per_punt"]'
}

BOXSCORE_RETRY = {
    'kickoff_return_touchdowns': 'td[data-stat="kick_ret_td"]',
    'punt_return_touchdowns': 'td[data-stat="punt_ret_td"]'
}

RANKINGS_SCHEME = {
    'name': 'td[data-stat="school_name"]',
    'week': 'th[data-stat="week_poll"]',
    'date': 'td[data-stat="date_poll"]',
    'rank': 'td[data-stat="rank"]',
    'previous': 'td[data-stat="rank_prev"]',
    'change': 'td[data-stat="rank_diff"]'
}

SEASON_PAGE_URL = 'http://www.sports-reference.com/cfb/years/%s-standings.html'

OFFENSIVE_STATS_URL = ('https://www.sports-reference.com/cfb/years/'
                       '%s-team-offense.html')
DEFENSIVE_STATS_URL = ('https://www.sports-reference.com/cfb/years/'
                       '%s-team-defense.html')

SCHEDULE_URL = ('https://www.sports-reference.com/cfb/schools/%s/'
                '%s-schedule.html')

BOXSCORE_URL = 'https://www.sports-reference.com/cfb/boxscores/%s.html'

BOXSCORES_URL = ('https://www.sports-reference.com/cfb/boxscores/index.cgi'
                 '?month=%s&day=%s&year=%s&conf_id=')
CONFERENCES_URL = 'https://www.sports-reference.com/cfb/years/%s.html'
CONFERENCE_URL = 'https://www.sports-reference.com/cfb/conferences/%s/%s.html'
CFP_RANKINGS_URL = 'https://www.sports-reference.com/cfb/years/%s-polls.html'
RANKINGS_URL = 'https://www.sports-reference.com/cfb/years/%s-polls.html'
PLAYER_URL = 'https://www.sports-reference.com/cfb/players/%s.html'
ROSTER_URL = 'https://www.sports-reference.com/cfb/schools/%s/%s-roster.html'
