#
# Copyright (C) 2021-2022 by @Shahm_Sport@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @SH_AH_M
# Rocks © @Shayri_Music_Lovers
# Owner Shahm
# Harshit Sharma
# All rights reserved. © Abbas © SHAHM


import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print(
        "\nها هي جلسة سلسلة Pyrogram الخاصة بك ، انسخها ، لا تشاركها مع احد ابدا حتى وان ادعى انه مطور من مطورين سورس شهم الخاص بك!\n"
    )
    print(f"\n{ss}\n")


asyncio.run(main())
