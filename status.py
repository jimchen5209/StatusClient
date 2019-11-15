#  StatusClient by jimchen5209
#  Copyright (C) 2019-2019
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function

import json
import os
import sys
from pathlib import Path


class Status:
    __path = str(Path.home()) + '/.bot_status'

    def __init__(self, name: str):
        self.__data = {
            'name': name,
            'pid': os.getpid(),
            'cmdline': sys.argv,
            'online': False
        }
        self.__filename = name.replace(" ", "_")

    def set_status(self, online: bool):
        self.__data['online']= online
        if os.path.isdir(self.__path):
            with open("{path}/{name}.json".format(path=self.__path, name=self.__filename), 'w', encoding='UTF-8') as fs:
                json.dump(self.__data, fs, ensure_ascii=False)
