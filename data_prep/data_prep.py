import json

def match_summary(json_file : dict):


    # Extracting match summary info
    city = json_file['info'].get('city','unknown')
    teams=json_file['info']['teams']
    match_name = json_file['info']['event']['name']
    match_number = json_file['info']['event']['match_number']
    winner = json_file['info']['outcome'].get('winner','draw')
    by = ''.join(['by ' + str(v) + ' ' + str(k) for k,v in json_file['info']['outcome'].get('by','unknown').items()])
    pom = ''.join(json_file['info'].get('player_of_match','None'))

    match_desc = f'''Match of tournament {match_name} carrying match number {match_number} was played in {city} between {teams[0]} and {teams[1]} . The winner of the match was {winner}. {winner} won {by}. Player of the match was {pom}.'''
    return match_desc

def over_summary(json_file : dict):

    #Extracting per over summary
    teams = json_file['info']['teams']
    chunks = []

    for innings_idx, innings in enumerate(json_file.get('innings')):
        batting_team = innings.get("team")
        bowling_team = teams[1] if teams[0]==batting_team else teams[0]

        for ov in innings.get('overs'):
            over_num = ov.get('over')
            runs_in_the_over = 0
            wickets_in_the_over = 0
            extras_in_the_over = 0
            ball_descriptions = []


            for ball in ov.get('deliveries'):
                ball_num = ball.get("actual_delivery")
                batter = ball.get("batter")
                bowler = ball.get("bowler")
                runs = ball.get("runs", {})
                wickets = ball.get("wickets", [])
                extras = ball.get("extras")

                runs_in_the_over += int(runs.get("total"))

                desc = f"Ball {ball_num}: {bowler} bowls to {batter}, scoring {runs.get('batter')} runs (Total runs from delivery: {runs.get('total')})."

                if wickets:
                    wickets_in_the_over += len(wickets)
                    for w in wickets:
                        desc += f" [WICKET] {w.get('player_out')} was dismissed ({w.get('kind')})."
                
                ball_descriptions.append(desc)

            over_text = (
                f"Innings context: {batting_team} batting vs {bowling_team}.\n"
                f"Over Number: {over_num}\n"
                f"Summary of Over: {runs_in_the_over} runs scored, {wickets_in_the_over} wickets taken.\n"
                + "\n".join(ball_descriptions)
            )

            chunks.append(over_text)
    return '\n'.join(chunks)

def file_read():
    with open('../1000851.json','r',encoding="utf-8") as f:
        data_new = json.load(f)
        # print(match_summary(data_new))
        # print(over_summary(data_new)[:5])


if __name__ == "__main__":
    file_read()