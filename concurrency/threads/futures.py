import time
from concurrent.futures import Future, ThreadPoolExecutor


def square(item: int) -> int:
    # simulate a computation by sleeping
    time.sleep(5)
    return item * item


def square2(item: int) -> int:
    return item // 0


def square3(item: int) -> int:
    return item * item


def my_special_callback(ftr: Future[int]) -> None:
    res = ftr.result()
    print(f"my_special_callback invoked {res}")


def my_other_special_callback(ftr: Future[int]) -> None:
    res = ftr.result()
    print(f"my_other_special_callback invoked {res * res}")


def main() -> None:
    # print("1st example")
    # executor = ThreadPoolExecutor(max_workers=10)

    # future = executor.submit(square, 7)

    # print(f"is running : {future.running()}")
    # print(f"is done : {future.done()}")
    # print(f"Attempt to cancel : {future.cancel()}")
    # print(f"is cancelled : {future.cancelled()}")

    # executor.shutdown()

    # print("2nd example")
    # executor = ThreadPoolExecutor(max_workers=1)

    # future = executor.submit(square2, 7)
    # ex = future.exception()
    # print(ex)

    # executor.shutdown()

    # print("3rd example")
    # executor = ThreadPoolExecutor(max_workers=1)

    # _ = executor.submit(square, 7)
    # future2 = executor.submit(square, 9)

    # print(f"is running : {future2.running()}")
    # print(f"is done : {future2.done()}")
    # print(f"Attempt to cancel : {future2.cancel()}")
    # print(f"is cancelled : {future2.cancelled()}")

    # executor.shutdown()

    print("4th example")
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square3, 7)
    future.add_done_callback(my_special_callback)
    future.add_done_callback(my_other_special_callback)

    executor.shutdown(wait=False)


if __name__ == "__main__":
    main()
