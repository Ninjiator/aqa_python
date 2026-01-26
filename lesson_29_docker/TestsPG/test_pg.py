from psycopg2.extras import RealDictCursor
import pytest


@pytest.mark.parametrize("email, name",[
    ("user_insert@gmail.com", "user_insert")
])
def test_insert_and_select(conn, email, name):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "INSERT INTO users (email, name) VALUES (%s, %s) RETURNING id, email, name;",
            (email, name))
        created_user = cur.fetchone()
        conn.commit()


        assert created_user["id"] == 1
        assert created_user["email"] == email
        assert created_user["name"] == name


        cur.execute("SELECT id, email, name FROM users WHERE id=%s;", (created_user["id"],))
        row = cur.fetchone()
        assert row == created_user


@pytest.mark.parametrize("email, name", [
    ("user_update@.com", "user_update")
])
def test_update(conn, email, name):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        #inserting user data
        cur.execute(
            "INSERT INTO users (email, name) VALUES (%s, %s) RETURNING id, email, name;",
            (email, name))

        #saving user ID with new data
        created_user_id = cur.fetchone()["id"]
        conn.commit()

        new_user_name = "Mikel"
        cur.execute("UPDATE users SET name=%s WHERE id=%s RETURNING id, email, name",
                    (new_user_name, created_user_id))
        #user data from RETURNING
        updated_user_row = cur.fetchone()
        conn.commit()

        assert updated_user_row["name"] == new_user_name
        assert updated_user_row["email"] == email

        cur.execute("SELECT id, email, name FROM users WHERE id=%s;", (created_user_id,))
        user_after_commit = cur.fetchone()
        #comparing RETURNING data with data on DB
        assert updated_user_row == user_after_commit



@pytest.mark.parametrize("email, name", [
    ("user_delete@gmail.com", "user_delete")
])
def test_delete(conn, email, name):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("INSERT INTO users (email, name) VALUES (%s, %s) RETURNING id, email, name;",
                    (email, name))
        created_user_id = cur.fetchone()["id"]
        conn.commit()

        cur.execute("DELETE FROM users WHERE id=%s RETURNING id;",
                    (created_user_id,))
        deleted_user = cur.fetchone()
        conn.commit()

        assert deleted_user["id"] == created_user_id

        cur.execute("SELECT id FROM users WHERE id=%s;",
                    (created_user_id,))
        row = cur.fetchone()
        assert row is None

