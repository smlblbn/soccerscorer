// wto eleminated string attribute sql

Select Match.id, Country.name,  League.name, Match.B365A, Match.B365D, Match.B365H, Match.BSA, Match.BSD, Match.BSH, Match.BWA, Match.BWD, Match.BWH, Match.GBA, Match.GBD, Match.GBH, Match.IWA,
Match.IWD, Match.IWH, Match.LBA, Match.LBD, Match.LBH, Match.PSA, Match.PSD, Match.PSH, Match.SJA, Match.SJD, Match.SJH, Match.VCA, Match.VCD, Match.VCH, Match.WHA, Match.WHD, Match.WHH,
Team_Attributes.buildUpPlayDribbling, Team_Attributes.buildUpPlayDribblingClass, Team_Attributes.buildUpPlayPassing, Team_Attributes.buildUpPlayPassingClass, 
Team_Attributes.buildUpPlayPositioningClass, Team_Attributes.buildUpPlaySpeed, Team_Attributes.buildUpPlaySpeedClass, Team_Attributes.chanceCreationCrossing, Team_Attributes.chanceCreationCrossingClass, 
Team_Attributes.chanceCreationPassing, Team_Attributes.chanceCreationPassingClass, Team_Attributes.chanceCreationPositioningClass, Team_Attributes.chanceCreationShooting, Team_Attributes.chanceCreationShootingClass, 
Team_Attributes.defenceAggression, Team_Attributes.defenceAggressionClass, Team_Attributes.defenceDefenderLineClass, Team_Attributes.defencePressure, Team_Attributes.defencePressureClass, 
Team_Attributes.defenceTeamWidth, Team_Attributes.defenceTeamWidthClass, t.buildUpPlayDribbling, t.buildUpPlayDribblingClass, t.buildUpPlayPassing, t.buildUpPlayPassingClass, 
t.buildUpPlayPositioningClass, t.buildUpPlaySpeed, t.buildUpPlaySpeedClass, t.chanceCreationCrossing, t.chanceCreationCrossingClass, 
t.chanceCreationPassing, t.chanceCreationPassingClass, t.chanceCreationPositioningClass, t.chanceCreationShooting, t.chanceCreationShootingClass, 
t.defenceAggression, t.defenceAggressionClass, t.defenceDefenderLineClass, t.defencePressure, t.defencePressureClass, 
t.defenceTeamWidth, t.defenceTeamWidthClass, Match.home_team_goal, Match.away_team_goal
FROM Match 
INNER JOIN Country ON Match.country_id=Country.id INNER JOIN League ON Country.id=League.country_id 
INNER JOIN Team_Attributes ON Match.home_team_api_id=Team_Attributes.team_api_id
AND Match.date > Team_Attributes.date INNER JOIN Team_Attributes as t ON Match.away_team_api_id=t.team_api_id 
AND Match.date > t.date GROUP BY Match.id

// one league sql

Select Match.B365A, Match.B365D, Match.B365H, Match.BWA, Match.BWD, Match.BWH, Match.IWA,
Match.IWD, Match.IWH, Match.LBA, Match.LBD, Match.LBH, Match.VCA, Match.VCD, Match.VCH, Match.WHA, Match.WHD, Match.WHH,
Team_Attributes.buildUpPlayPassing, Team_Attributes.buildUpPlaySpeed, Team_Attributes.chanceCreationCrossing, 
Team_Attributes.chanceCreationPassing, Team_Attributes.chanceCreationShooting, 
Team_Attributes.defenceAggression, Team_Attributes.defencePressure,  
Team_Attributes.defenceTeamWidth, t.buildUpPlayPassing,  
t.buildUpPlaySpeed, t.chanceCreationCrossing, 
t.chanceCreationPassing,  t.chanceCreationShooting, 
t.defenceAggression,  t.defencePressure, 
t.defenceTeamWidth,  Match.home_team_goal, Match.away_team_goal
FROM Match 
INNER JOIN Country ON Match.country_id=Country.id INNER JOIN League ON Country.id=League.country_id 
INNER JOIN Team_Attributes ON Match.home_team_api_id=Team_Attributes.team_api_id
AND Match.date > Team_Attributes.date INNER JOIN Team_Attributes as t ON Match.away_team_api_id=t.team_api_id 
AND Match.date > t.date WHERE League.name=="England Premier League" GROUP BY Match.id

// full veri sql

Select Match.B365A, Match.B365D, Match.B365H, Match.BWA, Match.BWD, Match.BWH, Match.IWA,
Match.IWD, Match.IWH, Match.LBA, Match.LBD, Match.LBH, Match.VCA, Match.VCD, Match.VCH, Match.WHA, Match.WHD, Match.WHH,
Team_Attributes.buildUpPlayPassing, Team_Attributes.buildUpPlaySpeed, Team_Attributes.chanceCreationCrossing, 
Team_Attributes.chanceCreationPassing, Team_Attributes.chanceCreationShooting, 
Team_Attributes.defenceAggression, Team_Attributes.defencePressure,  
Team_Attributes.defenceTeamWidth, t.buildUpPlayPassing,  
t.buildUpPlaySpeed, t.chanceCreationCrossing, 
t.chanceCreationPassing,  t.chanceCreationShooting, 
t.defenceAggression,  t.defencePressure, 
t.defenceTeamWidth,  Match.home_team_goal, Match.away_team_goal
FROM Match 
INNER JOIN Country ON Match.country_id=Country.id INNER JOIN League ON Country.id=League.country_id 
INNER JOIN Team_Attributes ON Match.home_team_api_id=Team_Attributes.team_api_id
AND Match.date > Team_Attributes.date INNER JOIN Team_Attributes as t ON Match.away_team_api_id=t.team_api_id 
AND Match.date > t.date WHERE League.name!="Poland Ekstraklasa" AND League.name!="Switzerland Super League" GROUP BY Match.id



