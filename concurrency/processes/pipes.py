import multiprocessing as mp
import time
from multiprocessing.connection import PipeConnection


def child_process(conn: PipeConnection) -> None:
    for i in range(10):
        conn.send(f"hello {i + 1}")
    conn.close()


def main() -> None:
    parent_conn, child_conn = mp.Pipe()  # duplex=True by default
    p = mp.Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(3)

    for _ in range(10):
        msg = parent_conn.recv()  # recv is blocking
        print(msg)

    parent_conn.close()
    p.join()


if __name__ == "__main__":
    main()
