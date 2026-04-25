import grpc

from examples import user_service_pb2_grpc, user_service_pb2

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Отправляем запрос
response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
print(response.message)  # Выведет: Привет, Alice!
