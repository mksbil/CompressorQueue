#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("28015531", default=6, cast=int)
    API_HASH = config("2ab4ba37fd5d9ebf1353328fc915ad28", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("7296815871:AAHBoe7szXTXc7i5CDYNGWgWrfqJbm0e5i4")
    DEV = 6121610691
    OWNER = config("6121610691")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset veryfast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
