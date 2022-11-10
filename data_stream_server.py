from concurrent import futures

import grpc

import data_stream_service_pb2_grpc
import data_stream_service_pb2
from db import db_helper


class UserDataServicer(data_stream_service_pb2_grpc.DataStreamServicer):
    def GetUserByID(self, request, context):
        _data = db_helper.get_user(id=request.id)[0]
        data = data_stream_service_pb2.UserData()
        data.name = _data.name
        data.email = _data.email
        data.username = _data.username
        data.phone_number = _data.phone_number
        return data

    def GetUserList(self, request, context):
        _datas = db_helper.get_user()
        _user_data = data_stream_service_pb2.UserDataList()
        for _data in _datas:
            data = data_stream_service_pb2.UserData()
            data.name = _data.name
            data.email = _data.email
            data.username = _data.username
            data.phone_number = _data.phone_number
            _user_data.list.append(data)
        return _user_data


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_stream_service_pb2_grpc.add_DataStreamServicer_to_server(UserDataServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
