
import asyncio
import unittest

from tests.log_function import log_to_stdout


class TestExample(unittest.IsolatedAsyncioTestCase):

    async def test_logging(self):
        logs = []
        with self.assertLogs() as captured:
            task = asyncio.create_task(log_to_stdout())
            await asyncio.sleep(62)
            for i in captured.records:
                if i.getMessage() == "This line should be logged every 1 minute":
                    self.assertEqual(i.getMessage(), "This line should be logged every 1 minute")
                    logs.append(i)
        self.assertEqual(len(logs), 2)
        time = int(logs[1].created) - int(logs[0].created)
        self.assertEqual(time, 60)
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("Task Cancelled already")

