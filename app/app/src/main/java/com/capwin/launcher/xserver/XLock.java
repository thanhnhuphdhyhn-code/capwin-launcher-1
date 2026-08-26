package com.capwin.launcher.xserver;

public interface XLock extends AutoCloseable {
    @Override
    void close();
}
