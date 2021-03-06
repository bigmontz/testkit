import nutkit.protocol as protocol

from .session import Session


class Driver:
    def __init__(self, backend, uri, authToken):
        self._backend = backend
        req = protocol.NewDriver(uri, authToken)
        res = backend.sendAndReceive(req)
        if not isinstance(res, protocol.Driver):
            raise "Should be driver"
        self._driver = res

    def close(self):
        req = protocol.DriverClose(self._driver.id)
        res = self._backend.sendAndReceive(req)
        if not isinstance(res, protocol.Driver):
            raise "Should be driver"

    def session(self, accessMode, bookmarks=None):
        req = protocol.NewSession(self._driver.id, accessMode, bookmarks)
        res = self._backend.sendAndReceive(req)
        if not isinstance(res, protocol.Session):
            raise "Should be session"
        return Session(self._backend, res)
