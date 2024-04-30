import time
from db import db_session
from db.user import User
from db.Score.leaderBoard import LeaderBoard

db_session.global_init("db/users.db")
while True:
    session = db_session.create_session()
    for i in session.query(User).all():
        d = {}
        for j in i.userTestAttempts:
            if j.test_id not in d:
                d[j.test_id] = 0
            d[j.test_id] = max(j.right_percent * j.test.testScore[0].max_score, d[j.test_id])
        answer = 0
        for j in d.keys():
            answer += d[j]
        a = session.query(LeaderBoard).filter(LeaderBoard.user_id == i.id).first()
        if not a:
            lb = LeaderBoard(
                user_id=i.id,
                score=answer,
                tests_passed=len(d.keys())
            )
            session.add(lb)
        else:
            a.score = answer
            a.tests_passed = len(d.keys())
        session.commit()
    session.close()
    time.sleep(60)
