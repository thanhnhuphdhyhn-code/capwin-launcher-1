package com.capwin.launcher.xserver.events;

import com.capwin.launcher.xconnector.XOutputStream;
import com.capwin.launcher.xconnector.XStreamLock;
import com.capwin.launcher.xserver.Window;

import java.io.IOException;

public class MapRequest extends Event {
    private final Window parent;
    private final Window window;

    public MapRequest(Window parent, Window window) {
        super(20);
        this.parent = parent;
        this.window = window;
    }

    @Override
    public void send(short sequenceNumber, XOutputStream outputStream) throws IOException {
        try (XStreamLock lock = outputStream.lock()) {
            outputStream.writeByte(code);
            outputStream.writeByte((byte)0);
            outputStream.writeShort(sequenceNumber);
            outputStream.writeInt(parent.id);
            outputStream.writeInt(window.id);
            outputStream.writePad(20);
        }
    }
}
