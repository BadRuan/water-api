from asyncio import run
from core.service import get_waterlevel_1, get_waterlevel_2
from core.util import filePath, save_xlsx1, save_xlsx2


async def test_table1():
    stations = await get_waterlevel_1()
    filepath = filePath("table1", "dist1")
    await save_xlsx1(filepath[0], filepath[1], stations)


async def test_table2():
    stations = await get_waterlevel_2()
    filepath = filePath("table2", "dist2")
    await save_xlsx2(filepath[0], filepath[1], stations)


async def main():
    await test_table1()
    await test_table2()

if __name__ == "__main__":
    print("----测试开始----")
    run(main())
    print("----测试结束----")
