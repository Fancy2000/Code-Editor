from concurrent import futures
import psycopg2
import grpc
import service_pb2_grpc
import service_pb2


class WriteUser:
    name: str
    surname: str


write_user = WriteUser()


def start_connection():
    conn = psycopg2.connect(
        database='postgres', user='postgres', password='password', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    return conn, cursor


def close_connection(cursor, conn):
    cursor.close()
    conn.close()


def update_text(cursor, conn, room_id, text):
    cursor.execute(f"UPDATE users SET text = '{text}' WHERE room_id = '{room_id}';")
    conn.commit()


def get_new_text(cursor, conn, room_id) -> str:
    print("IN SERVER::get_new_text()")
    cursor.execute(f"SELECT text FROM users WHERE room_id = '{room_id}' and writer = true;")
    conn.commit()
    res = cursor.fetchall()
    print(res)
    if res:
        return res[0][0]
    return "No text"


def get_role(cursor, conn, login, password, room_id):
    cursor.execute(f"SELECT writer FROM users WHERE room_id = '{room_id}'"
                   f" and user_login = '{login}' and user_password = '{password}';")
    conn.commit()
    return cursor.fetchall()


class Message(service_pb2_grpc.MessageServicer):

    def UpdateRole(self, request, ctx):
        print("IN UPADATE ROLE---------")
        room_id = request.room_id
        name = request.name
        surname = request.surname
        role = request.role
        conn, cursor = start_connection()

        cursor.execute(f"SELECT * FROM users WHERE room_id = '{room_id}' and writer = true;")
        conn.commit()
        is_writer = cursor.fetchall()
        print(is_writer)
        cursor.execute(f"SELECT writer FROM users WHERE room_id = '{room_id}'"
                       f" and user_name = '{name}' and user_surname = '{surname}';")
        conn.commit()
        tmp_res = cursor.fetchall()[0][0]
        print(tmp_res)
        if tmp_res and role == "writer":
            print("keep writer")
            print("--------------------------------")
            close_connection(cursor, conn)
            return service_pb2.NewRoleResponse(role="writer")
        if tmp_res and role == "reader":
            cursor.execute(f"UPDATE users SET writer = false WHERE room_id = '{room_id}';")
            conn.commit()
            close_connection(cursor, conn)
            print("set tmp read in 1 if")
            print("--------------------------------")
            return service_pb2.NewRoleResponse(role="reader but can be writer")

        print("IN UPDAte role check new writer")
        if len(is_writer) == 0 and role == "reader but can be writer":
            print("Set new writer")
            cursor.execute(f"UPDATE users SET writer = true WHERE room_id = '{room_id}'"
                           f" and user_name = '{name}' and user_surname = '{surname}';")
            conn.commit()
            close_connection(cursor, conn)
            print("--------------------------------")
            return service_pb2.NewRoleResponse(role="writer")

        if len(is_writer) == 0 and role == "reader":
            print("Set tmp reader")
            close_connection(cursor, conn)
            print("--------------------------------")
            return service_pb2.NewRoleResponse(role="reader but can be writer")

        close_connection(cursor, conn)
        print("set just a reader")
        print("--------------------------------")
        return service_pb2.NewRoleResponse(role="reader")

    def Registration(self, request, ctx):
        print("--------------------------------")
        print("IN Registration")
        log = request.login
        pas = request.password
        name = request.name
        surname = request.surname
        # establishing the connection
        conn, cursor = start_connection()
        print("CONNECTION OK")
        # Preparing query to create a database
        cursor.execute("SELECT array_agg(user_login), array_agg(user_password) FROM users ;")
        conn.commit()
        check_user = cursor.fetchall()

        print("Login: " + log)
        print("password: " + pas)
        print(check_user)
        if check_user != [(None, None)]:
            for i in range(len(check_user[0][0])):
                login, password = check_user[0][0][i], check_user[0][1][i]
                if log == login and password == pas:
                    close_connection(cursor, conn)
                    print("Registration FALSE", flush=True)
                    print("--------------------------------")
                    return service_pb2.RegistrateResponse(code=43, info="This user already exists, please try again")
        cursor.execute(f"INSERT INTO users (user_login, user_password, user_name, user_surname) VALUES ('{log}', '{pas}', '{name}', '{surname}');")
        conn.commit()
        close_connection(cursor, conn)
        print("DISCONNECTION OK")

        print("Registration OK", flush=True)
        print("--------------------------------")
        return service_pb2.RegistrateResponse(code=0, info=f"Registration completed! Welcome {name} {surname}", name=name, surname=surname)

    def LogIn(self, request, ctx):

        print("--------------------------------")
        print("in login")
        log = request.login
        pas = request.password
        # establishing the connection
        conn, cursor = start_connection()

        # Preparing query to create a database
        cursor.execute("SELECT array_agg(user_login), array_agg(user_password) FROM users ;")
        conn.commit()
        check_user = cursor.fetchall()

        print(check_user)

        print("Login: " + log)
        print("password: " + pas)
        if check_user == [(None, None)]:
            close_connection(cursor, conn)
            print("LOGIN FALSE", flush=True)
            print("--------------------------------")
            return service_pb2.LogInResponse(code=43, info="Please do registration.")

        for i in range(len(check_user[0][0])):
            login, password = check_user[0][0][i], check_user[0][1][i]
            print("get log: " + login)
            print("get pas: " + password)
            if login == log and password == pas:
                cursor.execute(f"SELECT array_agg(user_name), array_agg(user_surname) FROM users WHERE user_login = '{log}' AND user_password = '{pas}';")
                conn.commit()
                name, surname = cursor.fetchall()[0]
                name = name[0]
                surname = surname[0]
                print("name: ", name)
                print("surname: ", surname)
                # Closing the connection
                close_connection(cursor, conn)
                print("LOGIN OK", flush=True)
                print("--------------------------------")
                return service_pb2.LogInResponse(code=0, info=f"Welcome back {name} {surname}", name=name,
                                                 surname=surname)

        # Closing the connection
        close_connection(cursor, conn)
        print("LOGIN FALSE", flush=True)
        print("--------------------------------")
        return service_pb2.LogInResponse(code=43, info="Incorrect login or password. Please try again.")

    def GetListOfUsers(self, room_id_req, ctx):
        print("IN server::GetListOfUsers")
        conn, cursor = start_connection()
        room_id = room_id_req.room_id
        name_of_user = room_id_req.name
        surname_of_user = room_id_req.surname
        text = room_id_req.text
        print("text from code_mirror: " + text)
        cursor.execute(f"SELECT array_agg(user_name), array_agg(user_surname) FROM users WHERE room_id = '{room_id}';")
        conn.commit()
        list_of_users = cursor.fetchall()
        res = []
        for name, surname in zip(list_of_users[0][0], list_of_users[0][1]):
            res.append(service_pb2.Users(name=name, surname=surname))

        print("name: " + name_of_user)
        print("surname: " + surname_of_user)
        print("room_id: " + room_id)
        cursor.execute(f"SELECT writer FROM users WHERE room_id = '{room_id}'"
                       f" and user_name = '{name_of_user}' and user_surname = '{surname_of_user}';")
        conn.commit()
        is_writer = cursor.fetchall()
        print(is_writer)
        if is_writer[0][0]:
            print("user is writer")
            update_text(cursor, conn, room_id, text)
        else:
            print("user is not writer")
            text = get_new_text(cursor, conn, room_id)
        close_connection(cursor, conn)
        return service_pb2.ListOfUsers(list_of_users=res, text=text)

    def GetUserWhoWrite(self, empty, cxt):
        return service_pb2.WriteUserResponse(name=write_user.name, surname=write_user.surname)

    def SetUserWhoWrite(self, user, cxt):
        write_user.name = user.name
        write_user.surname = user.surname
        return service_pb2.Empty()

    def SetRoomId(self, room_id_req, cxt):
        print("IN SERVE::SetRoomId()")
        conn, cursor = start_connection()
        room_id = room_id_req.room_id
        req_name = room_id_req.name
        req_surname = room_id_req.surname
        req_log = room_id_req.login
        req_pas = room_id_req.password
        cursor.execute(f"SELECT * FROM users WHERE room_id = '{room_id}'"
                       f" and user_name = '{req_name}' and user_surname = '{req_surname}'"
                       f"and user_login = '{req_log}' and user_password = '{req_pas}';")
        conn.commit()
        res = cursor.fetchall()
        print(res)
        if not res:
            req_text = get_new_text(cursor, conn, room_id)
            print("req_text")
            print(req_text)
            if req_text == "No text":
                cursor.execute(f"SELECT * FROM users WHERE room_id = '{room_id}';")
                conn.commit()
                res = cursor.fetchall()
                if not res:
                    cursor.execute(f"INSERT INTO users (user_login, user_password,"
                               f" user_name, user_surname, room_id, writer, text) VALUES"
                               f" ('{req_log}', '{req_pas}', '{req_name}', '{req_surname}', '{room_id}', true , '');")
                    conn.commit()
            else:
                cursor.execute(f"INSERT INTO users (user_login, user_password,"
                            f" user_name, user_surname, room_id, writer, text) VALUES"
                                f" ('{req_log}', '{req_pas}', '{req_name}', '{req_surname}', '{room_id}', false ,'{req_text}');")
                conn.commit()
            cursor.execute(f"DELETE FROM users WHERE writer is NULL;")
            conn.commit()
            print("after get role")

            role = get_role(cursor, conn, req_log, req_pas, room_id)
            close_connection(cursor, conn)
            print(role[0][0])
            ans_role = "reader"
            if role[0][0]:
                ans_role = "writer"
            return service_pb2.RoomIdLogResponse(name="", surname="", role=ans_role)

        cursor.execute(f"SELECT array_agg(user_name), array_agg(user_surname) FROM users WHERE room_id is NULL;")
        conn.commit()
        name_and_surname = cursor.fetchall()
        if name_and_surname == [(None, None)]:

            role = get_role(cursor, conn, req_log, req_pas, room_id)
            close_connection(cursor, conn)
            ans_role = "reader"
            if role:
                ans_role = "writer"
            return service_pb2.RoomIdLogResponse(name="", surname="", role=ans_role)
        print(name_and_surname)
        cursor.execute(f"UPDATE users SET room_id = '{room_id}' WHERE room_id IS NULL;")
        cursor.execute(f"SELECT array_agg(user_name), array_agg(user_surname) FROM users WHERE room_id = '{room_id}';")
        conn.commit()
        list_of_users = cursor.fetchall()
        print(list_of_users[0][0])
        if len(list_of_users[0][0]) == 1:
            cursor.execute(f"UPDATE users SET writer = true WHERE writer IS NULL;")
        else:
            cursor.execute(f"UPDATE users SET writer = false WHERE writer IS NULL;")
        conn.commit()
        role = get_role(cursor, conn, req_log, req_pas, room_id)
        ans_role = "reader"
        if role:
            ans_role = "writer"
        close_connection(cursor, conn)

        name = name_and_surname[0][0][0]
        surname = name_and_surname[0][1][0]

        return service_pb2.RoomIdLogResponse(name=name, surname=surname, role=ans_role)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MessageServicer_to_server(Message(), server)
    server.add_insecure_port('[::]:8888')
    server.start()
    server.wait_for_termination()


serve()
