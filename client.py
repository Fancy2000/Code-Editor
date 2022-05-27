import grpc
import service_pb2_grpc
import service_pb2


class Client:

    def __init__(self):
        channel = grpc.insecure_channel('localhost:8888')
        self.stub = service_pb2_grpc.MessageStub(channel)

    def Registration(self, login: str, password: str, name: str, surname: str) -> [int, str]:
        ans = self.stub.Registration(service_pb2.RegistrateRequest(
            login=login, password=password, name=name, surname=surname
        ))
        return [ans.code, ans.info]

    def Login(self, login: str, password: str) -> [int, str, str, str]:
        ans = self.stub.LogIn(service_pb2.LogInRequest(login=login, password=password))
        return [ans.code, ans.info, ans.name, ans.surname]

    def GetListOfUsers(self, room_id, text, name, surname) -> [service_pb2.ListOfUsers]:
        ans = self.stub.GetListOfUsers(service_pb2.RoomIdRequest(room_id=room_id, name=name,
                                                                 surname=surname, text=text))
        return ans

    def GetUserHwoWrite(self) -> [str, str]:
        ans = self.stub.GetUserWhoWrite(service_pb2.Empty())
        return [ans.name, ans.surname]

    def SetUserWhoWrite(self, name, surname):
        self.stub.GetUserWhoWrite(service_pb2.WriteUserResponse(name=name, surname=surname))

    def SetRoomId(self, room_id, name, surname, login, password):
        print("in setroom")
        res = self.stub.SetRoomId(service_pb2.RoomIdLogRequest(room_id=room_id, name=name, surname=surname, login=login,
                                                               password=password))
        return res.name, res.surname, res.role

    def Update_Role(self, name, surname, room_id, role):
        res = self.stub.UpdateRole(service_pb2.NewRoleRequest(room_id=room_id, name=name, surname=surname, role=role))
        return res.role
