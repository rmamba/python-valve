# -*- coding: utf-8 -*-

from __future__ import (absolute_import,
                        unicode_literals, print_function, division)

import pytest
import six

import valve.rcon


class TestRust(object):

    @pytest.mark.timeout(timeout=3, method="thread")
    def test_authenticate(self):
        rcon = valve.rcon.RCON(('192.168.1.69', 29015), b"vaSSago@23104375")
        with rcon as rcon:
            assert rcon.authenticated is True

    @pytest.mark.timeout(timeout=3, method="thread")
    def test_execute(self):
        rcon = valve.rcon.RCON(('192.168.1.69', 29015), b"vaSSago@23104375")
        rcon.connect()
        rcon._authenticated = True
        response = rcon.execute("echo hello")
        assert response.id == 0
        assert response.type is response.Type.RESPONSE_VALUE
        assert response.body == b"hello"
        assert isinstance(response.body, six.binary_type)

    @pytest.mark.timeout(timeout=3, method="thread")
    def test_call(self):
        rcon = valve.rcon.RCON(('192.168.1.69', 29015), b"vaSSago@23104375")
        rcon.connect()
        rcon._authenticated = True
        response = rcon("echo hello")
        assert response == "hello"
        assert isinstance(response, six.text_type)
