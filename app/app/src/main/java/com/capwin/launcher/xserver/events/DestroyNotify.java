package com.capwin.launcher.xserver.events;

import com.capwin.launcher.xconnector.XOutputStream;
import com.capwin.launcher.xconnector.XStreamLock;
import com.capwin.launcher.xserver.Window;

import java.io.IOException;

public class DestroyNotify extends Event {
    private final Window event;
    private final Window window;

    public DestroyNotify(Window event, Window window) {
        super(17);
        this.event = event;
        this.window = window;
    }

    @Override
    public void send(short sequenceNumber, XOutputStream outputStream) throws IOException {
        try (XStreamLock lock = outputStream.lock()) {
            outputStream.writeByte(code);
            outputStream.writeByte((byte)0);
            outputStream.writeShort(sequenceNumber);
            outputStream.writeInt(event.id);
            outputStream.writeInt(window.id);
            outputStream.writePad(20);
        }
    }
}
