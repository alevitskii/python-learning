import asyncio
import random
from threading import current_thread

BLOCK = 4096


class ChatServer:
    def __init__(self, port: int) -> None:
        self.port = port
        self.clients: dict[str, asyncio.StreamWriter] = {}
        self.writers: dict[asyncio.StreamWriter, str] = {}

    async def handle_client(self, message: str, writer: asyncio.StreamWriter) -> None:
        command, param = message.split(",")

        if command == "register":
            print(f"\n{param} registered -- {current_thread().name}\n")
            self.clients[param] = writer
            self.writers[writer] = param

            # send ack
            writer.write("ack".encode())
            await writer.drain()

        if command == "chat":
            to_writer = None
            if param in self.clients:
                to_writer = self.clients[param]

            if to_writer is not None:
                to_writer.write(f"{self.writers[writer]} says hi".encode())
                await to_writer.drain()
            else:
                print(f"\nNo user by the name |{param}|\n")

        if command == "list":
            names = ",".join(self.clients)
            writer.write(names.encode())
            await writer.drain()

    async def run_server(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        while True:
            data = await reader.read(BLOCK)
            message = data.decode()
            print(f"\nserver received: {message} -- {current_thread().name}\n")

            await self.handle_client(message, writer)


class User:
    def __init__(self, name: str, server_host: str, server_port: int):
        self.name = name
        self.server_port = server_port
        self.server_host = server_host

    async def receive_messages(self, reader: asyncio.StreamReader) -> None:
        while 1:
            message = (await reader.read(BLOCK)).decode()
            print(f"\n{self.name} received: {message} -- {current_thread().name}\n")

    async def run_client(self) -> None:
        reader, writer = await asyncio.open_connection(
            self.server_host, self.server_port
        )

        # register
        writer.write(f"register,{self.name}".encode())
        await writer.drain()
        await reader.read(BLOCK)

        # get list of friends
        writer.write("list,friends".encode())
        await writer.drain()
        friends_ = (await reader.read(BLOCK)).decode()
        print(f"Received {friends_}")

        # launch coroutine to receive messages
        asyncio.create_task(self.receive_messages(reader))

        friends = friends_.split(",")
        num_friends = len(friends)

        while 1:
            friend = friends[random.randint(0, num_friends - 1)]
            print(f"{self.name} is sending msg to {friend} -- {current_thread().name}")
            writer.write(f"chat,{friend}".encode())
            await writer.drain()
            await asyncio.sleep(3)


async def main() -> None:
    server_port = random.randint(10000, 65000)
    server_host = "127.0.0.1"
    chat_server = ChatServer(server_port)
    jane = User("Jane", server_host, server_port)
    zak = User("Zak", server_host, server_port)

    server = await asyncio.start_server(
        chat_server.run_server, server_host, server_port
    )
    asyncio.create_task(jane.run_client())
    asyncio.create_task(zak.run_client())

    await server.serve_forever()


if __name__ == "__main__":
    # start server
    asyncio.run(main())
