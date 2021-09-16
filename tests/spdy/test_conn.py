# Copyright (C) 2021 Mathew Odden
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import base64
import unittest
import io


from spdy import conn as spdy


class FramerTestCase(unittest.TestCase):
    def test_read_frames(self):
        test_data = """
        gAMAAQAAACkAAAABAAAAAAAAePnjxqfCYmBgYASns5Ki1MRcaFHCmgoKaAAAAAD//4ADAAEAAAAX
        AAAAAwAAAAAAAMIuVVySkpkHAAAA//+AAwABAAAAGQAAAAUAAAAAAADCKsVWXJKSX1oCAAAA//+A
        AwABAAAAGAAAAAcAAAAAAADCLleUWpxZlQoAAAD//wAAAAcAAAAaeyJXaWR0aCI6MTgyLCJIZWln
        aHQiOjMwfQoAAAADAAAAAWwAAAADAAAAAXMAAAADAAAAASAAAAADAAAAAS0AAAADAAAAAWwAAAAD
        AAAAAWEAAAADAAAAAQ0AAAADAAAAAWUAAAADAAAAAXgAAAADAAAAAWkAAAADAAAAAXQAAAADAAAA
        AQ2AAwADAAAACAAAAAMAAAAFgAMAAwAAAAgAAAAFAAAABYADAAMAAAAIAAAABwAAAAWAAw==
        """
        test_data = test_data.replace("\n", "").replace(" ", "")
        test_data = base64.b64decode(test_data)

        data_stream = io.BytesIO(test_data)
        frames = None
        stream = spdy.Framer()

        data = True
        while data:
            data = data_stream.read(1024)
            if data:
                frames = stream.read_frames(data)
            else:
                break

        self.assertIsNotNone(frames)
        self.assertEqual(len(frames), 20)
