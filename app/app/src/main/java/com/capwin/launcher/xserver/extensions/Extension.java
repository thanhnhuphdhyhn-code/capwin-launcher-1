package com.capwin.launcher.xserver.extensions;

import com.capwin.launcher.xconnector.XInputStream;
import com.capwin.launcher.xconnector.XOutputStream;
import com.capwin.launcher.xserver.XClient;
import com.capwin.launcher.xserver.XServer;
import com.capwin.launcher.xserver.errors.XRequestError;

import java.io.IOException;

public abstract class Extension {
    public static final byte START_MAJOR_OPCODE = -100;
    private final byte majorOpcode;
    protected final XServer xServer;

    public Extension(XServer xServer, byte majorOpcode) {
        this.xServer = xServer;
        this.majorOpcode = majorOpcode;
    }

    public abstract String getName();

    public byte getMajorOpcode() {
        return majorOpcode;
    }

    public byte getFirstErrorId() {
        return 0;
    }

    public byte getFirstEventId() {
        return 0;
    }

    public abstract void handleRequest(XClient client, XInputStream inputStream, XOutputStream outputStream) throws IOException, XRequestError;
}
