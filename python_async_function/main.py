#!/usr/bin/env python3

import asyncio
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

# Run the measure_time coroutine and print its result
async def main():
    result = await measure_time(n, max_delay)
    print(result)

# Start the event loop
asyncio.run(main())