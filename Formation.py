import Utils as ut
import numpy as np

#Get Frame data for given match_id, team_id and framenumber
connection = ut.DbConnection()
result = connection.query('DFL-MAT-0028OW', 'DFL-CLU-000002', 24690)
print('10 Spieler: \n', result)
