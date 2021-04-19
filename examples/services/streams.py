import asyncio
import logging
from pathlib import Path

from symphony.bdk.core.config.loader import BdkConfigLoader
from symphony.bdk.core.symphony_bdk import SymphonyBdk
from symphony.bdk.gen.pod_model.stream_filter import StreamFilter
from symphony.bdk.gen.pod_model.stream_type import StreamType
from symphony.bdk.gen.pod_model.v3_room_attributes import V3RoomAttributes


async def run():
    stream_id = "ubaSiuUsc_j-_lVQ8vhAz3___opSJdJZdA"

    config = BdkConfigLoader.load_from_symphony_dir("config.yaml")

    async with SymphonyBdk(config) as bdk:
        streams = bdk.streams()

        stream = await streams.create_im_or_mim([13056700579872, 13056700579891, 13056700579850])
        room = await streams.create_room(V3RoomAttributes(name="New fancy room", description="test room"))

        logging.debug(await streams.get_stream(stream_id))
        await streams.add_member_to_room(13056700579859, stream_id)
        await streams.remove_member_from_room(13056700579859, stream_id)

        async for m in await streams.list_all_streams_members(stream_id):
            print(m)

        stream_filter = StreamFilter(
            stream_types=[StreamType(type="IM"), StreamType(type="MIM"), StreamType(type="ROOM")],
            include_inactive_streams=False)
        async for s in await streams.list_all_streams(stream_filter):
            print(s)


logging.config.fileConfig(Path(__file__).parent.parent / "logging.conf", disable_existing_loggers=False)

asyncio.run(run())
