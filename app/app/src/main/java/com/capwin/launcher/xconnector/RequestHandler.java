package com.capwin.launcher.xconnector;

import java.io.IOException;

public interface RequestHandler {
    boolean handleRequest(ConnectedClient client) throws IOException;
}
