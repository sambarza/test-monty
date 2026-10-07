import asyncio
import os

from pathlib import Path, PurePosixPath

from pydantic_monty import Monty, load_snapshot, os_access, CallbackFile
from pydantic_monty import MemoryFile, OSAccess, MountDir

THIS_DIR = Path(__file__).parent
SANDBOX_CODE_PATH = THIS_DIR / "sandbox_code.py"
DATA_DIR = Path(__file__).parent / "data"

def read_fn(path: PurePosixPath) -> str:
    return f'content from {path}'

def write_fn(path: PurePosixPath, content: str | bytes) -> None:
    pass

os_access = OSAccess(
    # files = [
    #     MemoryFile("/data/customers/customers.csv", content="customers_csv"),
    #     MemoryFile("/etc/sample.txt", content="sample"),
    # ]
    [
        CallbackFile('/test/file.txt', read=read_fn, write=write_fn)
    ]
)


async def run():

    m = await Monty.acreate(SANDBOX_CODE_PATH.read_text())

    progress = m.start(
        # inputs={"url": "https://example.com"},
        # mount=MountDir("/data", DATA_DIR, mode="read-only"),
        # os=os_access
    )

    print(progress)

    # # Serialize the execution state
    # state = progress.dump()

    # # Later, restore and resume (e.g., in a different process)
    # progress2 = load_snapshot(state)

    # snapshot = progress2.resume(
    #     {"return_value": "response data"},
    #     mount=MountDir("/data", DATA_DIR, mode="read-only"),
    #     os=os_access,
    # )
    # print(snapshot)

    # > response data


def main():
    asyncio.run(run())

main()
