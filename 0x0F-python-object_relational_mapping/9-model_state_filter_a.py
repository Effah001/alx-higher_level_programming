states_a = session.query(State).filter(State.name.like('%a%')).all()
