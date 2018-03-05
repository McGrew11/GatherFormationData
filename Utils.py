import pyhdb
import numpy as np

class DbConnection:

    def deleteGoalkeeper(self, players):
        result = players
        x = players[:, 0]
        min = x.min()
        index = np.where(x == min)[0][0]
        array = np.delete(result, index, 0)
        return array

    def query(self, matchId, teamId, frame):
        try:
            connection = pyhdb.connect(host="sports-ml.mo.sap.corp",
                                       port=30015,
                                       user="SYSTEM",
                                       password="Toor1234")

            cursor = connection.cursor()

            selectStatement = "select x,y from \"SAP_SPORTS_DFL\".\"sap.sports.dfl.module.matchdata.private.table::TRACKING\" where match_id=%s and team_id=%s and n=%s"
            result = cursor.execute(selectStatement, [matchId, teamId, frame])

            res = cursor.fetchall()

            for i in res:
              print('[',i[0],',',i[1],']')

            players = []

            for i in res:
                players.append([float(i[0].real), float(i[1].real)])

            players = np.array(players)

            players = self.deleteGoalkeeper(players)
            return players

            connection.commit()
            connection.close()

        except Exception as e:
            print(e)
            connection.rollback()
            connection.close()
